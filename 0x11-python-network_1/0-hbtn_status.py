#!/usr/bin/python3
""" Fetching URLs with urllib """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-internet.hbtn.io/status') as request:
        response = request.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
                .format(type(html), html, html.decode('utf-8')))
