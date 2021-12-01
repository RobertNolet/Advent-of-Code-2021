#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 09:27:07 2021

@author: robertnolet
"""


data = [int(x) for x in open('input.txt')]

# Part 1
print(sum(x - y > 0 for x,y in zip(data[1:], data[:-1])))

# Part 2
print(sum(x - y > 0 for x,y in zip(data[3:], data[:-3])))
