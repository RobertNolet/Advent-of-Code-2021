#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:03:23 2021

@author: robertnolet
"""

# Player 1 starting position: 9
# Player 2 starting position: 3

# Part 1
def move(p, s, d, n, m):
    p = (p+d-1)%10 + 1
    return p, s+p, (d+7)%10 + 1, n+3, 1-m

p = [9,3] # Starting positions
s = [0,0] # Starting scores
d = [6,5] # Starting dice rolls mod 10
n = m = 0
while max(s) < 1000:
    p[m], s[m], d[m], n, m = move(p[m], s[m], d[m], n, m)
print(min(s)*n)

# Part 2
# Dict of possible 3 quantum die sums, with number of possibilities to
# obtain this roll.
rolls = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

def play(p, s = [0,0], m = 0):
    wins = [0,0]
    for d, v in rolls.items():
        oldp = p[m]
        p[m] = (p[m] + d - 1)%10 + 1
        s[m] += p[m]
        if s[m] >= 21: wins[m] += v
        else: 
            w0, w1 = play(p, s, 1-m)
            wins[0] += v*w0
            wins[1] += v*w1
        s[m] -= p[m]
        p[m] = oldp
    return wins

print(max(play([9,3])))