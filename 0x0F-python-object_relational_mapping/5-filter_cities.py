#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that accepts a state name as an extra argument and displays all the
    cities registered in that state in the given database
"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cursor = conn.cursor()
    q = "SELECT cities.name FROM cities JOIN states WHERE states.name = '{}'"
    q += " AND states.id = cities.state_id ORDER BY cities.id"
    q = q.format(args[4].replace("'", ""))
    cursor.execute(q)
    items = cursor.fetchall()
    cities = []
    for item, in items:
        cities.append(item)
    print(", ".join(cities))
