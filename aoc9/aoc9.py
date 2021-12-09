#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:41:40 2021

@author: robertnolet
"""

import numpy as np
from math import prod

# Read data
data = np.array([[int(n) for n in list(line.strip())] for line in open('input.txt')])
n,m = data.shape

# Return set of neighbouring coordinates, within bounds
def nbrs(i,j):
    return {(x, y) for x, y in {(i-1,j),(i+1,j),(i,j-1),(i,j+1)} if 0 <= x < n and 0 <= y < m}

# Check if point (i,j) is a local minimum
def lowpoint(i, j):
    return all(data[x,y] > data[i,j] for (x,y) in nbrs(i,j))

# Find all local minima
lows = np.array([[lowpoint(i,j) for j in range(m)] for i in range(n)])

# Part 1
print(data[lows].sum() + lows.sum())

# Part 2
sizes = []        # Top 3 basin sizes
checked = set()   # Set of all coordinates already part of a basin
for i,j in zip(*np.where(lows)):
    # Do we have multiple local minima in the same basin?
    if (i,j) not in checked:
        size = 1
        tocheck = nbrs(i,j) 
        checked.add((i,j))
        while tocheck:
            x, y = tocheck.pop()
            if data[x,y] != 9:                
                size += 1
                tocheck |= nbrs(x,y) - checked
                checked.add((x,y))
                
        if len(sizes) < 3:
            sizes.append(size)
        elif size > min(sizes):
            sizes.remove(min(sizes))
            sizes.append(size)
    
print(prod(sizes))
    
    