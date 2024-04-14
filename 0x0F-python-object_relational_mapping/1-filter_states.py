#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that accesses a mysql database using MySQLdb and lists all states
    starting with 'N' from states table. The user, password, and database to
    access are given as command line arguments
"""
import sys
import MySQLdb


if __name__ == '__main__':
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY id"
    cursor.execute(query)
    items = cursor.fetchall()
    for item in items:
        print(item)
    cursor.close()
    conn.close()
