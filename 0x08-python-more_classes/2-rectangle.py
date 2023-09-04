#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
    @property
    def width(self):
        """ Getter """
        return self.__width
    @width.setter
    def width(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter """
        return self.__height
    @height.setter
    def height(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= o")
        else:
            self.__height = value
    def area(self):
        """ return rectangle area """
        return (self.__height  * self.__width)
    def perimeter(self):
        """ return rectangle area """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))
