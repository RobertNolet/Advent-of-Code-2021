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
    
def numroutes(x, visits, revisit = False):
    n = 0
    for y in conn[x]:
        if y == 'end': n += 1
        elif y.isupper() or y not in visits or (revisit and y != 'start'):
            v = visits.copy()
            v[y] = v.get(y,0)+1
            n += numroutes(y, v, revisit and (y.isupper() or v[y] == 1))
    return n

# Part 1
print(numroutes('start', {'start':1}))

# Part 2
print(numroutes('start', {'start':1}, True))            
        