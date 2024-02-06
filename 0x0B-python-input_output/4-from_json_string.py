#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-from_json_string.py

Author: Yunus Kedir

This module contains:

Functions:
    from_json_string - Returns the Python object that a JSON string represents

"""


import json


def from_json_string(my_str):
    """Returns the Python object that a given JSON string deserializes to.

    Uses json module's loads method. Not all JSON strings are deserializable
    . If a non-deserializable string is passed, the method will raise an error.

    Args:
        my_str (str): A JSON string.

    Returns:
        The object that my_str deserializes to (if it deserializes to a valid
        python object).
    """
    return (json.loads(my_str))
