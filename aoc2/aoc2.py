#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:42:00 2021

@author: robertnolet
"""

dirs = {'forward':(1,0), 'back':(-1,0), 'up':(0,-1), 'down':(0, 1)}

def parse(line):
    d, n = line.split()
    dx, dy = dirs[d]
    return dx*int(n), dy*int(n)

data = [parse(line) for line in open('input.txt')]

# Part 1
dxs, dys = zip(*data)
print(sum(dxs)*sum(dys))

# Part 2
y = 0
aim = 0
for dx, dy in data:
    aim += dy
    y += dx*aim
print(sum(dxs)*y)
    