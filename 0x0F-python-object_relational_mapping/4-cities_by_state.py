#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

Author: Yunus Kedir

Contains:
    script that accesses a given database and joins states and cities tables to
    display desired records
"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cursor = conn.cursor()
    q = "SELECT cities.id, cities.name, states.name FROM cities JOIN states"
    q += " WHERE cities.state_id = states.id ORDER BY cities.id"
    cursor.execute(q)
    items = cursor.fetchall()
    for item in items:
        print(item)
