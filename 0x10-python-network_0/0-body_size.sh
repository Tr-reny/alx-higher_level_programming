#!/bin/bash

# This script takes in a URL as its first argument and uses curl to send a request to that URL with the "-sI" options (silent, head only).
# The response headers are piped to grep, which searches for the "Content-Length" field, which gives the size of the body in bytes.
# This value is then printed using awk.

curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
