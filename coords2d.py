#!/usr/bin/env python2.7

import math

class Coords2D():
    def __init__(self, a1, a2=None):
        if a2 is None:
            x, y = a1
        else:
            x, y = a1, a2

        self.x = x
        self.y = y

    def dist(self, other):
        return abs(self - other)

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __cmp__(self, other):
        if self.x == other.x and self.y == other.y:
            return 0
        else:
            return 1

    def __repr__(self):
        return "<Coords2D>: %s, %s" % (repr(self.x), repr(self.y))

    def __sub__(self, other):
        return Coords2D((self.x - other.x, self.y - other.y))
    
    def __add__(self, other):
        return Coords2D((self.x + other.x, self.y + other.y))

    def __mul__(self, other):
        if isinstance(other, Coords2D):
            return Coords2D((self.x * other.x, self.y * other.y))
        else: 
            return Coords2D((self.x * other, self.y * other))

    def __div__(self, other):
        if isinstance(other, float):
            return Coords2D((float(self.x) / other, float(self.y) / other))
        else:
            return Coords2D((self.x / other, self.y / other))

    def __iter__(self):
        return iter((self.x, self.y))

    def astuple(self):
        return self.x, self.y

