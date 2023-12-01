#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('utf-8')
    url = sys.argv[1]

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
