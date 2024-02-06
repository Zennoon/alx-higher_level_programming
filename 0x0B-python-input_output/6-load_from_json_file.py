#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-load_from_json_file.py

Author: Yunus Kedir

This module contains:

Functions:
    load_from_json_file - Extracts a python object from a JSON file

"""


import json


def load_from_json_file(filename):
    """Extracts a Python object from a JSON string in a file of given name.

    Args:
        filename (str): Name of the file to read the JSON string from.

    Returns:
        A python object that the JSON string inside the file represents
        if possible.
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        return (json.load(f))
