#!/usr/bin/python3
"""
    Module for getting the X-Request-Id of intranet.hbtn.io/status.
"""
import requests
import sys

if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp is not None:
        print(resp.headers.get('X-Request-Id'))
