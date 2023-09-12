#!/usr/bin/python3
"""Defines a file- appending function."""
def append_write(filename="", text=""):
    """append a string at the end of a text file (UTF*)
    and return the number of charcters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
