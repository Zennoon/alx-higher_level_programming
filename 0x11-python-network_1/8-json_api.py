#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Sends a POST request to a given url along with a given letter and displays
    response body if it is a valid JSON
"""
import requests
import sys


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    val = ""
    if len(sys.argv) >= 2:
        val = sys.argv[1]
    res = requests.post(url, data={'q': val})
    try:
        if res.text.strip() == '{}':
            print("No result")
        else:
            print("[{}] {}".format(res.json().get('id'),
                                   res.json().get('name')))
    except Exception as e:
        print("Not a valid JSON")
