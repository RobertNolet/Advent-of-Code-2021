#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:44:22 2021

@author: robertnolet
"""

import re
import numpy as np

def inbounds(x1, x2, y1, y2, z1, z2):
    return (-50 <= x1 <= x2 <= 50 and
            -50 <= y1 <= y2 <= 50 and
            -50 <= z1 <= z2 <= 50)

# Read data
pat = re.compile('(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
def parse(line):
    s, x1, x2, y1, y2, z1, z2 = pat.match(line).groups()
    return 1 if s == 'on' else 0, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)

data = [parse(line) for line in open('input.txt')]

# Part 1
initcube = np.zeros((101,101,101), dtype = int)
for s, x1, x2, y1, y2, z1, z2 in data:
    if inbounds(x1, x2, y1, y2, z1, z2):
        initcube[x1+50:x2+51,
                 y1+50:y2+51,
                 z1+50:z2+51] = s
print(initcube.sum())


# Part 2

# Find alls x,y,z coordinates and sort them. Our new grid will have
# elements of size dx * dy * dz.
xs, ys, zs = set(), set(), set()
for s, x1, x2, y1, y2, z1, z2 in data:
    if not inbounds(x1, x2, y1, y2, z1, z2):
        xs |= {x1, x2+1}
        ys |= {y1, y2+1}
        zs |= {z1, z2+1}
xs = sorted(xs)
ys = sorted(ys)
zs = sorted(zs)

# Calculate the volume of each grid element.
vol = np.tensordot(np.tensordot(np.diff(xs), np.diff(ys), axes=0), np.diff(zs), axes = 0)

# For each rule, find the index in the new grid, and set the corresponding cubes
grid = np.zeros(vol.shape, dtype = int)
for s, x1, x2, y1, y2, z1, z2 in data:
    if not inbounds(x1, x2, y1, y2, z1, z2):
        xi1 = xs.index(x1)
        xi2 = xs.index(x2+1)
        yi1 = ys.index(y1)
        yi2 = ys.index(y2+1)
        zi1 = zs.index(z1)
        zi2 = zs.index(z2+1)
        grid[xi1:xi2,yi1:yi2,zi1:zi2] = s
print((grid*vol).sum() + initcube.sum())