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
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
