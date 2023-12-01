#!/usr/bin/python3
""" Fetching URLs with urllib """

import urlib.request

if __name__ == "__main__":
    with urlib.request.urlopen('https://alx-intarnet.hbtn.io/status') as request:
        response = request.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
