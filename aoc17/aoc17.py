#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:47:28 2021

@author: robertnolet
"""

from math import ceil, floor, sqrt
from collections import defaultdict

xmin, xmax, ymin, ymax = 94, 151, -156, -103
#xmin, xmax, ymin, ymax = 20, 30, -10, -5   # Test case

# Part 1
vy = -ymin-1
print(vy**2 - (vy-1)*vy//2)

# Part 2
def realrange(xmin, xmax):
    return range(int(ceil(xmin)), int(floor(xmax))+1)
            
def x(t, vx):
    t = min(t, vx)
    return t*vx - (t-1)*t//2

# Make a dict of times, and list of y-velocities which are on
# target at that time.
ty = defaultdict(list)
for vy in range(ymin, -ymin):
    tmin = ((2*vy+1) + sqrt((2*vy+1)**2 - 8*ymax))/2
    tmax = ((2*vy+1) + sqrt((2*vy+1)**2 - 8*ymin))/2
    for t in realrange(tmin, tmax):
        ty[t].append(vy)
    
# Check for each x-velocity if it is in target at time when
# y can also be in target.
vs = set()
vxmin = (-1+sqrt(1+8*xmin))/2
vxmax = xmax
for vx in realrange(vxmin, vxmax):
    for t in ty:
        if xmin <= x(t, vx) <= xmax:
            vs |= {(vx, vy) for vy in ty[t]}
print(len(vs))