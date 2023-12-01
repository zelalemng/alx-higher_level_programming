#!/usr/bin/python3
""" Takes in a URL, sends a request to the URL and displays the body of the request"""
import requests
import sys

if __name__ == "__main__":
    error = requests.get(sys.argv[1])
    if error.ststus_code >= 400:
        print('Error code: {}'.format(error.status_code))
    else:
        print(error.text)
