#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 09:19:47 2021

@author: robertnolet
"""

import numpy as np
from itertools import product, combinations, permutations

# List of all rotations, including reflection
rotations = []
for i,j,k in permutations([0,1,2],3):
    for r,s,t in product([-1,1], repeat=3):
        m = np.zeros((3,3), int)
        m[0,i] = r
        m[1,j] = s
        m[2,k] = t
        rotations.append(m)

class ScanReport:
    def __init__(self, lines):
        self.name = lines[0]
        self.data = np.array([[int(n) for n in line.split(',')] for line in lines[1:]])
        self.n = len(self.data)
        self.dist = [(np.sum((self.data[i,:] - self.data[j,:])**2),i,j) for i,j in combinations(range(self.n),2)]
        self.rots = set(range(len(rotations)))
        self.pos = None
        
    def __str__(self):
        return self.name + '\n' + str(self.data)
        
    def commondist(self, other):
        a = {d for d,i,j in self.dist}
        b = {d for d,i,j in other.dist}
        return a & b

    def overlap(self, other):
        return len(self.commondist(other)) >= 66
                
reports = [ScanReport(block.split('\n')) for block in open('input.txt').read().split('\n\n')]

reports[0].pos = np.array([0,0,0])
found = [reports[0]]
tofind = reports[1:]

while tofind:
    for r1, r2 in product(found, tofind):
        if r1.overlap(r2):
            print(f"Testing {r1.name} and {r2.name}: ", end='')
            ds = r1.commondist(r2)
            for d in ds:
                # Find indices of points with common distance d, and the
                # corresponding difference vectors.
                i1, j1 = next((i,j) for dist,i,j in r1.dist if dist == d)    
                i2, j2 = next((i,j) for dist,i,j in r2.dist if dist == d)
                v1 = r1.data[i1,:] - r1.data[j1,:]
                v2 = r2.data[i2,:] - r2.data[j2,:]
                # Filter all rotations which wouldn't transform v2 into v1
                r2.rots -= {r for r in r2.rots if not np.all(v2.dot(rotations[r]) == v1)}
                if len(r2.rots) == 1: break
            if len(r2.rots) == 1:
                print("Transformation found!")
                rot = rotations[r2.rots.pop()]
                # If we found a reflection, we need to reverse i and j
                if np.linalg.det(rot) == -1: 
                    rot = -rot
                    i2, j2 = j2, i1
                # Rotate and translate r2
                r2.data = r2.data.dot(rot)
                r2.pos = r1.data[i1,:] - r2.data[i2,:]
                r2.data += r2.pos
                
                found.append(r2)
                tofind.remove(r2)
                break
            print("No luck...")


# Part 1            
print(len({(x,y,z) for r in reports for x,y,z in r.data}))          
                
# Part 2
print(max(np.sum(abs(r1.pos - r2.pos)) for r1, r2 in combinations(reports,2)))
