#!/usr/bin/python3
""" Fetching URLs with urllib """

import urllib.request


if __name__ == "__main__":
    response = request.read()

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as request:
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('UTF-8')))
