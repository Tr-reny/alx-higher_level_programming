#!/bin/bash
# Display the REQUEST options available on the server
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -d' ' -f2-
