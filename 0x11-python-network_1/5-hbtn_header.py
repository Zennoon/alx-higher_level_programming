#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Sends a request to a URL and displays the value of a given header
"""
import sys
import requests


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
