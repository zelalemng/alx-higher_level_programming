#!/usr/bin/python3
"""Takes in a URL and an email, seds a Post request
to the passed URL with the email as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    r = requests.post(sys.argv[1], data=email)
    print(r.text)
