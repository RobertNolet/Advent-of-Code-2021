#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:24:31 2021

@author: robertnolet
"""

from itertools import product
import numpy as np
import matplotlib.pyplot as plt

conv = {'.':0, '#':1}

line, data = open('input.txt').read().split('\n\n')

alg = [conv[c] for c in line.strip()]
img = np.array([[conv[c] for c in s.strip()] for s in data.split('\n')])

sub = list(product([-1,0,1],[-1,0,1]))

def bin2int(bs):
    return sum(b*2**(8-i) for i,b in enumerate(bs))

def enlarge(img, w):
    n,m = img.shape
    res = np.full((n+4,m+4), w)
    res[2:-2,2:-2] = img
    return res

def transform(img, alg):
    n,m = img.shape
    res =  np.zeros((n-2,m-2), dtype = int)
    for x in range(1,n-1):
        for y in range(1, m-1):
            res[x-1,y-1] = alg[bin2int([img[x+dx,y+dy] for dx,dy in sub])]
    return res

lights = []
w = 0
for i in range(50):
    img = transform(enlarge(img, w), alg)
    w = alg[0 if w == 0 else -1]
    lights.append(np.sum(img))
    if i in [1,49]: print(np.sum(img))
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.pause(0.5)
    plt.show()

plt.plot(range(50), lights, 'b-')