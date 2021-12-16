#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:39:05 2021

@author: robertnolet
"""

from math import prod

ops = {0:sum, 
       1:prod, 
       2:min, 
       3:max, 
       5:lambda ps: 1 if ps[0] > ps[1] else 0, 
       6:lambda ps: 1 if ps[0] < ps[1] else 0,
       7:lambda ps: 1 if ps[0] == ps[1] else 0}

class Stream:
    def __init__(self, data):
        self.data = data
        self.i = 0
        self.done = False
    
    def read(self, n):
        self.i += n
        if self.i == len(self.data):
            self.done = True
        return self.data[(self.i-n):self.i]
    
    def readint(self, n):
        return int(self.read(n), 2)
    
        
class Packet:
    def __init__(self, v, t):
        self.version = v
        self.typeID  = t
        
    def sumversion(self):
        return self.version
        
class Literal(Packet):
    def __init__(self, v, t, stream):
        super().__init__(v, t)
        s = ''
        while stream.read(1) == '1':
            s += stream.read(4)
        s += stream.read(4)
        self.val = int(s, 2)

    def value(self):
        return self.val
    
class Operator(Packet):
    def __init__(self, v, t, stream):
        super().__init__(v, t)
        if stream.read(1) == '0':
            s = Stream(stream.read(stream.readint(15)))
            self.packets = []
            while not s.done:
                self.packets.append(readpacket(s))
        else:
            self.packets = [readpacket(stream) for i in range(stream.readint(11))]
    
    def sumversion(self):
        return self.version + sum(p.sumversion() for p in self.packets)
    
    def value(self):
        return ops[self.typeID]([p.value() for p in self.packets])

def hex2bin(s):
    return ''.join(bin(int(c, 16))[2:].zfill(4) for c in s)
    
def readpacket(stream):
    v = stream.readint(3)
    t = stream.readint(3)
    if t == 4: 
        return Literal(v, t, stream)
    else: 
        return Operator(v, t, stream)
      
stream = Stream(hex2bin(open('input.txt').readline()))
p = readpacket(stream)
    
# Part 1
print(p.sumversion())
        
# Part 2
print(p.value())        