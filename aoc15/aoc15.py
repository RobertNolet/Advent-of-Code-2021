#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:15:28 2021

@author: robertnolet
"""

import numpy as np

dirs = [(0,1), (0, -1), (1, 0), (-1,0)]
data = np.array([[int(n) for n in line.strip()] for line in open('input.txt')])
n,m = data.shape

def valid(x,y, r=1):
    return 0 <= x < r*n and 0 <= y < r*m

def value(x, y):
    return (data[x % n, y % m] + x//n + y//m - 1)%9 + 1

# Dijkstra's algorithm
def solve(r=1):
    visited = set()
    tent = set()
    dist = {(0,0):0}
    x, y = 0, 0
    
    while (x, y) != (r*n-1, r*m-1):
        for dx, dy in dirs:
            if valid(x+dx, y+dy, r) and (x+dx,y+dy) not in visited:
                d = dist[x,y] + value(x+dx,y+dy)
                d = min(dist.get((x+dx,y+dy), d), d)
                dist[x+dx,y+dy] = d
                tent.add((d, x+dx, y+dy))
        visited.add((x,y))
        l, x, y = min(tent)
        tent.remove((l, x, y))
    return l
                
# Part 1
print(solve())

# Part 2
print(solve(5))
