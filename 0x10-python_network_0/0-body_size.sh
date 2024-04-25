#!/bin/bash
# Curls a given url and displays size of the body of the response
curl -sI "$1" | grep -E "Content-Length: .*" | cut -d ":" -f2 | tr -d " "
