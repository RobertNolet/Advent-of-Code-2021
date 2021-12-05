#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:11:45 2021

@author: robertnolet
"""

import re

pat = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
data = [[int(n) for n in pat.match(line).groups()] for line in open('input.txt')]

def sign(z):
    return 1 if z > 0 else -1 if z < 0 else 0

def solve(data, part):
    points = {}
    for x1, y1, x2, y2 in data:
        dx = sign(x2-x1)
        dy = sign(y2-y1)
        if part == 2 or x1 == x2 or y1 == y2:
            for i in range(max(abs(x2-x1), abs(y2-y1)) + 1):
                points[(x1+i*dx,y1+i*dy)] = points.get((x1+i*dx,y1+i*dy), 0)+1
    return sum(v > 1 for v in points.values())


# Part 1        
print(solve(data, 1))

# Part 2
print(solve(data, 2))
            