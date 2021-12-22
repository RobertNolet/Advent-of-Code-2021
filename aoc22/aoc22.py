#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:47:22 2021

@author: robertnolet
"""

import re
import numpy as np
from itertools import combinations, product

def inbounds(x1, x2, y1, y2, z1, z2):
    return (-50 <= x1 <= x2 <= 50 and
            -50 <= y1 <= y2 <= 50 and
            -50 <= z1 <= z2 <= 50)

def overlap(x11, x12, x21, x22):
    return not (x12 < x21 or x22 < x11)

def findoverlap(x11, x12, x21, x22):
    if x11 <= x21 <= x12 <= x22: return x21, x12
    if x21 <= x11 <= x22 <= x12: return x11, x22
    if x11 <= x21 <= x22 <= x12: return x21, x22
    if x21 <= x11 <= x12 <= x22: return x11, x12
    print(f"Unexpected overlap! x11 = {x11}, x12 = {x12}, x21 = {x21}, x22 = {x22}.")
    return None
    
    
class Cube:
    def __init__(self, v, x1, x2, y1, y2, z1, z2):
        self.v = v
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.connects = []
        self.group = None
    
    def value(self):
        return self.v * (self.x2-self.x1+1) * (self.y2-self.y1+1) * (self.z2-self.z1+1)
        
    def hasintersect(self, other):
        return (overlap(self.x1, self.x2, other.x1, other.x2) and
                overlap(self.y1, self.y2, other.y1, other.y2) and
                overlap(self.z1, self.z2, other.z1, other.z2))
    
    def intersect(self, other):
        x1, x2 = findoverlap(self.x1, self.x2, other.x1, other.x2)
        y1, y2 = findoverlap(self.y1, self.y2, other.y1, other.y2)
        z1, z2 = findoverlap(self.z1, self.z2, other.z1, other.z2)
        return Cube(-1, x1, x2, y1, y2, z1, z2)
        
    def assigngroup(self, group):
        self.group = group
        for cube in self.connects:
            if cube.group != group: 
                cube.assigngroup(group)
        
pat = re.compile('(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)')
def parse(line):
    s, x1, x2, y1, y2, z1, z2 = pat.match(line).groups()
    return 1 if s == 'on' else 0, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)
    
data = [parse(line) for line in open('test2.txt')]

# Part 1
initcube = np.zeros((101,101,101), dtype = int)
for s, x1, x2, y1, y2, z1, z2 in data:
    initcube[max(x1,-50)+50:min(x2,50)+51,
             max(y1,-50)+50:min(y2,50)+51,
             max(z1,-50)+50:min(z2,50)+51] = s
print(initcube.sum())

# Part 2
cubes = [Cube(*line) for line in data if not inbounds(*line[1:])]
for cube1, cube2 in combinations(cubes, 2):
    if cube1.hasintersect(cube2):
        cube1.connects.append(cube2)
        cube2.connects.append(cube1)
        
currentgroup = 0        
for cube in cubes:
    if not cube.group:
        cube.assigngroup(currentgroup)
        currentgroup += 1
    
        

             