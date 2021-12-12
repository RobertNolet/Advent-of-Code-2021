#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 09:30:09 2021

@author: robertnolet
"""

data = [line.strip().split('-') for line in open('input.txt')]
conn = {}
for a, b in data:
    conn[a] = conn.get(a, []) + [b]
    conn[b] = conn.get(b, []) + [a]
    
def numroutes(x, v, revisit = False):
    if x == 'end': return 1
    n = 0
    for y in conn[x]:
        if y.isupper() or v.get(y,0) == 0 or (revisit and y != 'start'):
            v[y] = v.get(y,0)+1
            n += numroutes(y, v, revisit and (y.isupper() or v[y] == 1))
            v[y] -= 1
    return n

# Part 1
print(numroutes('start', {'start':1}))

# Part 2
print(numroutes('start', {'start':1}, True))            
        