#!/bin/bash
# Curls a given URL and displays the body if status of response is 200
if ! [[ -z $(curl -sIL "$1" | grep "200") ]]; then curl -sL "$1"; fi;
