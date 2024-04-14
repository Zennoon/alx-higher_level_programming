#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script to list all states from a database given in the command line

"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    items = cursor.fetchall()
    for item in items:
        print(item)
    cursor.close()
    conn.close()
