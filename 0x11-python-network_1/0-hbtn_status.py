#!/usr/bin/python3
"""
    Module for getting the status of intranet.hbtn.io/status.
"""
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
            if resp is not None:
                html = resp.read()
                print("Body response:")
                print("\t- type: {}".format(type(html)))
                print("\t- content: {}".format(html))
                print("\t- utf8 content: {}".format(html.decode('utf-8')))
    except Exception:
        pass
