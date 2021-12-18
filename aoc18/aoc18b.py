#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:00:02 2021

@author: robertnolet
"""

import functools
from itertools import product

def parse(s):
    result = []
    depth = 0
    m = 1
    for c in s:
        if c == '[': 
            depth += 1
            m = m * 3
        if c == ',':
            m = m // 3 * 2
        if c == ']': 
            depth -= 1
            m = m // 2
        if c.isnumeric(): result.append([int(c), m, depth])
    return result

def explode(vds):
    for i, (v, m, d) in enumerate(vds):
        if d == 5:
            vds[i] = [0, m // 3, d-1]
            if i > 0: vds[i-1][0] += v
            v, m, d = vds.pop(i+1)
            if i+1 < len(vds): vds[i+1][0] += v
            return True
    return False

def split(vds):
    for i, (v,m,d) in enumerate(vds):
        if v > 9:
            vds[i] = [v-v//2, m*2, d+1]
            vds.insert(i,[v//2, m*3, d+1])
            return True
    return False

def reduce(vds):
    while (explode(vds) or split(vds)): pass
    return vds

def add(vds1, vds2):
    return reduce([[v, 3*m, d+1] for v,m,d in vds1]+[[v, 2*m, d+1] for v,m,d in vds2])

def magnitude(vds):
    return sum(m*v for (v, m, d) in vds)
    
data = [parse(line.strip()) for line in open('input.txt')]

# Part 1
print(magnitude(functools.reduce(add, data)))          

# Part 2
print(max(magnitude(add(a,b)) for a,b in product(data,data) if a != b))