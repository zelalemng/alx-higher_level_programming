#!/usr/bin/python3
""" Displays the value of the X-Request-Id variable
foundin the header of the response
"""

import urllib.request
import sys

if __name__ == "__main__":
    argument = sys.argv[1]

    request = urllib.request(argument)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
