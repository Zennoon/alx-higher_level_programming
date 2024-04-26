#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Sends a POST request to a given url with a custom header (email)
"""
import sys
import urllib
import urllib.request


if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode())
