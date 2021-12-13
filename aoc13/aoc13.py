#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:59:35 2021

@author: robertnolet
"""

import re
import matplotlib.pyplot as plt

data = open('input.txt').read()

pat = re.compile('(\d+),(\d+)')
dots = set((int(x), int(y)) for x,y in pat.findall(data))

pat = re.compile('fold along (x|y)=(\d+)')
folds = [(c, int(n)) for c,n in pat.findall(data)]
    
def foldx(dots, n):
    return {(x if x < n else 2*n - x, y) for x, y in dots}

def foldy(dots, n):
    return {(x, y if y < n else 2*n - y) for x, y in dots}

for i, (c, n) in enumerate(folds):
    dots = foldx(dots, n) if c == 'x' else foldy(dots, n)
    # Part 1
    if i==0: print(len(dots))

# Part 2
fig, ax = plt.subplots()
ax.plot(*list(zip(*dots)),'bo')
ax.set_aspect('equal')
ax.invert_yaxis()
plt.show()