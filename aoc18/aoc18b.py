#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:00:02 2021

@author: robertnolet
"""

from copy import deepcopy
import functools
from itertools import product

def parse(s):
    result = []
    depth = 0
    for c in s:
        if c == '[': depth += 1
        if c == ']': depth -= 1
        if c.isnumeric(): result.append([int(c), depth])
    return result

def explode(vds):
    for i, (v, d) in enumerate(vds):
        if d == 5:
            vds[i] = [0, d-1]
            if i > 0: vds[i-1][0] += v
            v, d = vds.pop(i+1)
            if i+1 < len(vds): vds[i+1][0] += v
            return True
    return False

def split(vds):
    for i, (v,d) in enumerate(vds):
        if v > 9:
            vds[i] = [v-v//2,d+1]
            vds.insert(i,[v//2,d+1])
            return True
    return False

def reduce(vds):
    while (explode(vds) or split(vds)): pass
    return vds

def add(vds1, vds2):
    return reduce([[v,d+1] for v,d in (vds1+vds2)])

def magnitude(vds):
    ms = deepcopy(vds)
    while len(ms)>1:
        d, i = min((-d, i) for i, (v,d) in enumerate(ms))
        ms.insert(i, [3*ms.pop(i)[0]+2*ms.pop(i)[0], -d-1])
    return ms[0][0]
    
data = [parse(line.strip()) for line in open('input.txt')]
n = len(data)

# Part 1
s = functools.reduce(lambda a,b: add(a,b), data)
print(magnitude(s))          

# Part 2
print(max(magnitude(add(a,b)) for a,b in product(data,data) if a != b))