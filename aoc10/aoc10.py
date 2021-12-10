#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:23:29 2021

@author: robertnolet
"""


pars = {')':'(', ']':'[', '>':'<', '}':'{'}
scores1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {'(':1, '[':2, '{':3, '<':4}


# Check if a line is incomplete or incorrect and return
# a (score, part) tuple
def score(line):
    ps = []
    for c in line:
        if c in pars:
            if pars[c] != ps.pop(): 
                # Line is incorrect, return a score for part 1
                return scores1[c], 1
        else:
            ps.append(c)
    # Line is incomplete, return a score for part 2
    return sum(scores2[c]*(5**i) for i, c in enumerate(ps)), 2


# Total score part 1    
s1 = 0
# List of scores part 2
s2 = []
# Read and score data
for line in open('input.txt'):
    s, part = score(line.strip())
    if part == 1: s1 += s
    if part == 2: s2.append(s)

# Part 1        
print(s1)

# Part 2
s2.sort()
print(s2[len(s2)//2])