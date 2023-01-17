#!/usr/bin/python3
"""
    Module for making POST request.
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    if resp is not None:
        print(resp.text)
