#!/bin/bash
# Curls a given URL with a custom header
curl -s -H "X-School-User-Id: 98" "$1"
