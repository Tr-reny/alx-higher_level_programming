#!/usr/bin/python3
"""
    Module for getting the status of intranet.hbtn.io/status.
"""
import requests

if __name__ == "__main__":
    resp = requests.get('https://intranet.hbtn.io/status')
    if resp is not None:
        print("Body response:")
        print("\t- type: {}".format(type(resp.text)))
        print("\t- content: {}".format(resp.text))
