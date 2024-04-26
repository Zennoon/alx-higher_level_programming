#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    Misc
    ====
    Lists the lase 10 commits of a given repo owned by a given user
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"
    res = requests.get(url.format(sys.argv[2], sys.argv[1]))
    commits = res.json()
    for i in range(10):
        if i < len(commits):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
