#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Sends github credentials (name and password) to API and displays ID
"""
import requests
import sys


if __name__ == '__main__':
    basic_auth = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("http://api.github.com/user", auth=basic_auth)
    print(res.json().get('id'))
