#!/usr/bin/python3
"""
    Module for performing a GET request and printing error code if it exist
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            if resp is not None:
                html = resp.read()
                print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
