#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""100-append_after.py

Author: Yunus Kedir

This module contains:

Functions:
    append_after - Appends a given string to a file in a new line each time some
                   string is found in the file. The line is added after the line
                   in which the search string was found.

"""


def append_after(filename="", search_string="", new_string=""):
    """Adds a given string to a file in a new line each time some string
    is found in the file. The line is added after the line in which the search
    string was found.

    Args:
        filename (str): Name of the file to be manipulated.
        search_string (str): The string which is looked for in each line.
        new_string (str): The new string to add in a new line each time the
                          search_string is found.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    for idx, line in enumerate(contents):
        if search_string in line:
            lines[idx] += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(''.join(lines))


append_after("file.txt", "python", "c\n")
