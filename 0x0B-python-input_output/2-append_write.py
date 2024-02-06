#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-append_write.py

Author: Yunus Kedir

This module contains:

Functions:
    append_write - Appends a given text string to a file with given name

"""


def append_write(filename="", text=""):
    """Appends a given string to a file with a given name.

    The string is added to the end of the file if it exists.

    Args:
        filename (str): Name of the file to append to.
        text (str): The text string to append to the file.

    Returns:
        int: The number of characters written(appended) to the file.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return (f.write(text))
