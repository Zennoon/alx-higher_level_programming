#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-read_file.py

Author: Yunus Kedir

This module contains:

Functions:
    read_file - Reads the content of a file of given name.

"""


def read_file(filename=""):
    """Prints out the contents of a text file of given name to stdout.

    Args:
        filename (str): Name of the file to open and read.
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")
