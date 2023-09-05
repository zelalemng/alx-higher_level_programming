#!/usr/bin/python3
"""
This is the "add Integer" modele.

tis module supplies one function add_integer(), which adds together 2 int or float types and returns an int.
"""
def add_integer(a, b=98):
    """Return the sum of two integers or floats as an integer.
    Otherwise raise a TypeError for given incorrect argument type.
    """
    h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))
    if all(h):
        return int(a) + int(b)
    for x, y in list(zip(h, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
