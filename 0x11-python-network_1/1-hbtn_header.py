#!/usr/bin/python3
"""
    Module to get response header value of a url.
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            if resp is not None:
                idr = resp.getheader('X-Request-Id')
            print(idr)
    except Exception:
        pass
