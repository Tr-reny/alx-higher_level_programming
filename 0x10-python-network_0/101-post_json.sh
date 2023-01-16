#!/bin/bash
# Send a POST request with JSON file
curl -s "$1" -X POST -H "Content-Type: application/json" -d "$(cat "$2")"
