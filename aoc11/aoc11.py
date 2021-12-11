#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:04:56 2021

@author: robertnolet
"""

import numpy as np
from itertools import product

# Read data
data = np.array([[int(n) for n in list(line.strip())] for line in open('input.txt')])
n, m = data.shape

# Run one time step, return number of flashed dumbos
def flash(data):
    data += 1
    toflash = set(zip(*np.where(data > 9)))
    flashed = set()
    while toflash:
        x,y = toflash.pop()
        flashed.add((x,y))
        # Increase energy of surroundings, and update to flash
        for dx, dy in product([-1,0,1], [-1,0,1]):
            if 0 <= x+dx < n and 0 <= y+dy < m and (x+dx,y+dy) not in flashed:
                data[x+dx,y+dy] += 1
                if data[x+dx,y+dy] > 9: toflash.add((x+dx,y+dy))
    # Reset all flashed dumbos
    data[np.where(data > 9)] = 0
    return len(flashed)

    
total, nflash, t = 0, 0, 0
while nflash != n*m:
    total += (nflash := flash(data))
    
    # Part 1
    if t == 100: print(total)
    t += 1

# Part 2
print(t)