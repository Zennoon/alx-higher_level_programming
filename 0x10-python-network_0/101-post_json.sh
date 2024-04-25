#!/bin/bash
# Curls a given URL with a POST request sending a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
