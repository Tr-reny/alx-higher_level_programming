#!/bin/bash

curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
