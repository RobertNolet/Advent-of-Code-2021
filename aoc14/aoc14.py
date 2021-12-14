#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 09:57:59 2021

@author: robertnolet
"""

import re
from collections import defaultdict

file = open('input.txt')

# Read the polymer
polymer = file.readline().strip()

# Count the number of pairs of letters
pcounts = defaultdict(int)
for a,b in zip(polymer[:-1], polymer[1:]): pcounts[a,b] += 1
    
# Read the rules, each rule converts one pair into two pairs    
pat = re.compile('(.)(.) -> (.)')
rules = {(a,b):((a,c), (c,b)) for a,b,c in pat.findall(file.read())}
 
def onestep(pcounts):
    newcounts = defaultdict(int)
    for k, (v1, v2) in rules.items():
        newcounts[v1] += pcounts[k]
        newcounts[v2] += pcounts[k]
    return newcounts

def score(pcounts):
    counts = defaultdict(int)
    for (a, b), n in pcounts.items():
        counts[a] += n
        counts[b] += n
    # We double counted every letter in each pair, except for the first and
    # and last letter in the polymer. Correct for this.
    counts[polymer[0]]  += 1
    counts[polymer[-1]] += 1
    return (max(counts.values()) - min(counts.values()))//2
                          
# Part 1
for t in range(10): pcounts = onestep(pcounts)
print(score(pcounts))

# Part 2
for t in range(10,40): pcounts = onestep(pcounts)
print(score(pcounts))