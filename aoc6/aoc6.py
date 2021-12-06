#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 09:15:29 2021

@author: robertnolet
"""

# Read data, count how many fish there are of ages 0 to 8
data = [0]*9
for n in open('input.txt').readline().split(','): data[int(n)] += 1

# Simulate one day
def oneday(data):
    spawn = data.pop(0)
    data[6] += spawn
    data.append(spawn)    
    
# Part 1    
for t in range(1,81): oneday(data)
print(sum(data))

# Part 2
for t in range(81, 257): oneday(data)
print(sum(data))
    