#!/usr/bin/python3
import dis
import math

class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    def area(self):
        return self.__raduis ** 2 * math.pi
    def circumference(self):
        return 2 * math.pi * self.__radius
