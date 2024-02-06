#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-write_file.py

Author: Yunus Kedir

This module contains:

Functions:
    write_file - Writes a given text string to a file with given name

"""


def write_file(filename="", text=""):
    """Writes a given string to a file with a given name.

    The file is created if it doesn't exist, and overwritten if it exists.

    Args:
        filename (str): Name of the file to write to.
        text (str): The text string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(text))
