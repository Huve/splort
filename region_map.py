#!/usr/bin/python
#
# April 3 2016

class RegionMap():
    def __init__(self, w=1024, h=768):
        self.w = w
        self.h = h
        self.tiles = {i:{j:"dirt_1" for j in range(h/64)} for i in range(w/64)}
        
