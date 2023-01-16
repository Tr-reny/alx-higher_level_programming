#!/bin/bash
# Display the size of the body of a response from curling a URL
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2
