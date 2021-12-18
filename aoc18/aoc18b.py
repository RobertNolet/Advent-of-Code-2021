#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:00:02 2021

@author: robertnolet
"""

import functools
from itertools import product

# Make list of value, magnitude and depths for all numbers in a line of input.
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

# Explode first pair at depth 5
def explode(vmds):
    for i, (v, m, d) in enumerate(vmds):
        if d == 5:
            vmds[i] = [0, m // 3, d-1]
            if i > 0: vmds[i-1][0] += v
            v, m, d = vmds.pop(i+1)
            if i+1 < len(vmds): vmds[i+1][0] += v
            return True
    return False

# Split first value greater than 9
def split(vmds):
    for i, (v,m,d) in enumerate(vmds):
        if v > 9:
            vmds[i] = [v-v//2, m*2, d+1]
            vmds.insert(i,[v//2, m*3, d+1])
            return True
    return False

# Apply explodes or splits until neither does anything
def reduce(vmds):
    while (explode(vmds) or split(vmds)): pass
    return vmds

# Add two lists of values, magnitudes and depths, adjust for the
# new depth level.
def add(vmds1, vmds2):
    return reduce([[v, 3*m, d+1] for v,m,d in vmds1]+[[v, 2*m, d+1] for v,m,d in vmds2])

# Calculate total magnitude
def magnitude(vmds):
    return sum(m*v for (v, m, d) in vmds)
    
data = [parse(line.strip()) for line in open('input.txt')]

# Part 1
print(magnitude(functools.reduce(add, data)))          

# Part 2
print(max(magnitude(add(a,b)) for a,b in product(data,data) if a != b))