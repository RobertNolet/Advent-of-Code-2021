#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 09:35:32 2021

@author: robertnolet
"""
import numpy as np

class Board:
    def __init__(self, file):
        self.v = np.array([[int(n) for n in file.readline().split()] for row in range(5)])
        self.m = np.full((5,5), False)
        self.won = False
        
    def mark(self, n):
        self.m[np.where(self.v == n)] = True
        self.won = np.any(self.m.all(axis=0)) or np.any(self.m.all(axis=1))
        
    def score(self):
        return np.sum(self.v[np.where(np.logical_not(self.m))])
    
    
# Read data
file = open('input.txt')
numbers = [int(n) for n in file.readline().split(',')]
boards = [Board(file) for line in file] # line is the newline before each board

# Play
scores = []
for n in numbers:
    for b in boards:
        if b.won: continue
        b.mark(n)
        if b.won:
            scores.append(b.score()*n)
                
# Print scores of first and last winning boards
print(scores[0], scores[-1])