#!/usr/bin/python3
""" Displays the value of the X-Request-Id variable foundin the header of the response"""
import urllib.request
import sys

if __name__ == "__main__":
    angument = sys.argv[1]
    with urllib.request.urlopen(argument) as response:
        print(response.hesders["X-Request-Id'])
