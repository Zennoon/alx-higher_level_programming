#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Sends request to given url and displays value of given header of response

"""
import sys
import urllib.request


with urllib.request.urlopen(sys.argv[1]) as res:
    print(res.info().get('X-Request-Id'))
