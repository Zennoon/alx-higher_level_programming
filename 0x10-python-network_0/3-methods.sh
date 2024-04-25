#!/bin/bash
# Curls a given URL with an OPTIONS request to see which methods are acceptable
curl -si -X OPTIONS "$1" | grep "Allow: " | sed 's/Allow: //'
