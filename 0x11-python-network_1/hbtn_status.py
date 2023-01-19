#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
from urllib.request import urlopen

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        html_bytes = response.read()
        html = html_bytes.decode()
        print("- " + html.replace("\n", "\n\t-"))
