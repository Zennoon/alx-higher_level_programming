#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Sends a request to a given URL and catches any HTTPErrors
"""
import sys
import urllib.request
from urllib.error import HTTPError


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
