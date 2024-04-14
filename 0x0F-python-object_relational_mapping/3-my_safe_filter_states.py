#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that accesses a mysql database using MySQLdb and lists all states
    matching a given name from states table. The user, password, database to
    access, and state name to search for are given as command line arguments
"""
import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cursor = conn.cursor()
    q = "SELECT * FROM states WHERE states.name = '{}' ORDER BY states.id"
    q = q.format(args[4].replace("'", ""))
    cursor.execute(q)
    items = cursor.fetchall()
    for item in items:
        if item[1][0].isupper():
            print(item)
    cursor.close()
    conn.close()
