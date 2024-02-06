#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5-save_to_json_file.py

Author: Yunus Kedir

This module contains:

Functions:
    save_to_json_file - Writes JSON string of Python object to a file.

"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the JSON string of a python object to a file.

    Args:
        my_obj: A python object, the JSON string of which is written to file.
        filename (str): Name of the file to write to.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
