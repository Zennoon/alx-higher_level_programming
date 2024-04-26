#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Script to fetch a URL and display its body
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    res_content = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(res_content)))
    print("\t- content: {}".format(res_content))
    print("\t- utf8 content: {}".format(res_content.decode('utf-8')))
