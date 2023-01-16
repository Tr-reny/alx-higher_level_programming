#!/bin/bash
# Curl a URL and display body if the status is 200
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then curl -sL "$1"; fi
