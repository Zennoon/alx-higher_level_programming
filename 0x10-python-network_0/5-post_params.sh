#!/bin/bash
# Curls a given URL with a POST request with some variables
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
