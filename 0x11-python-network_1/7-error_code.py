#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Sends a request to a given URL and displays the body if no client or server       \
     error (status code is lower than 400), otherwise displays error code
"""
import requests
import sys


if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
