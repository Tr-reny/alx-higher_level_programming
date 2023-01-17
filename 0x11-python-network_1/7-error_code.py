#!/usr/bin/python3
"""
    Module for making POST request.
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp is not None:
        if resp.status_code == requests.codes.ok:
            print(resp.text)
        else:
            print('Error code: {}'.format(resp.status_code))
