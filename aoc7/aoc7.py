#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:40:30 2021

@author: robertnolet
"""

from statistics import median, mean

data = [int(n) for n in open('input.txt').readline().split(',')]

# Part 1
m = int(median(data))
print(sum(abs(x - m) for x in data))

# Part 2
m = int(mean(data))
print(sum(abs(x-m)*(abs(x-m)+1) for x in data)//2)