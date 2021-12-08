#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:35:42 2021

@author: robertnolet
"""

letters = 'abcdefg'
data = [[[set(p) for p in q.strip().split()] for q in line.split('|')] for line in open('input.txt')]

# Part 1
print(sum(sum(len(p) in [2,3,4,7] for p in line[1]) for line in data))

# Part 2
result = 0
for signal, output in data:
    mapping = [None]*10
    
    # Count lengths of words in signal, and identify unique numbers 1,4,7 and 8
    lengths = [len(p) for p in signal]
    mapping[1] = signal[lengths.index(2)]
    mapping[4] = signal[lengths.index(4)]
    mapping[7] = signal[lengths.index(3)]
    mapping[8] = signal[lengths.index(7)]
    
    # Count letters in signal, and identify unique letters b, e, f
    counts = [sum(k in p for p in signal) for k in letters]    
    b = {letters[counts.index(6)]}
    e = {letters[counts.index(4)]}
    f = {letters[counts.index(9)]}
    
    # Identify the other letters
    a = mapping[7] - mapping[1]
    c = mapping[1] - f    
    d = mapping[4] - mapping[1] - b
    g = mapping[8] - a - b - c - d - e - f
    
    # Reconstruct the other numbers 
    mapping[0] = a|b|c|e|f|g
    mapping[2] = a|c|d|e|g
    mapping[3] = a|c|d|f|g
    mapping[5] = a|b|d|f|g
    mapping[6] = a|b|d|e|f|g
    mapping[9] = a|b|c|d|f|g
    
    # Translate output and add to result
    for i, q in enumerate(output):
        result += mapping.index(set(q))*10**(3-i) 
print(result)    
    
    
    