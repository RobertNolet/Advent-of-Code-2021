#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:07:35 2021

@author: robertnolet
"""

import numpy as np

# Convert a list of 0s and 1s into a number
def bin2int(xs):
    return sum(x*(2**i) for x,i in zip(xs, range(len(xs)-1,-1,-1)))


data = np.array([[int(m) for m in list(s.strip())] for s in open('input.txt')])
n, m = data.shape

# Part 1
counts = (data == 1).sum(axis=0)

gamma   = bin2int([1 if c > n - c else 0 for c in counts])
epsilon = bin2int([0 if c > n - c else 1 for c in counts])   
print(gamma*epsilon)
        
    
# Part 2

# Find oxygen rating (x == 1) or CO2 rating (x == 0)
def solve(x, data):
    for b in range(m):
        # Count number of 1's in column b
        c = (data[:,b] == 1).sum()
        
        # If 1's are in the majority, keep all rows with x in position b
        # else keep rows with (1-x)
        data = data[data[:,b] == x if c >= len(data) - c else 1-x,:]
        
        if len(data) == 1: break
    return bin2int(data[0,:])

print(solve(0, data)*solve(1, data))