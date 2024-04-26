#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus kedir

Contains:
    Misc
    ====
    Sends a POST request to a given URL with a parameter
"""
import requests
import sys


if __name__ == '__main__':
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
