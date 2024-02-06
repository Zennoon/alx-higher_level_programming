#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-to_json_string.py

Author: Yunus Kedir

This module contains:

Functions:
    to_json_string - Returns the JSON string representation of an object

"""

import json


def to_json_string(my_obj):
    """Returns the JSON string representation of a given Python object.

    Uses the standard json module's dumps function. Not all Python objects
    are serializable. If a non-serializable object is passed, the module
    the method will raise an exception.

    Args:
        my_obj: The object whose JSON string is returned (if serializable).

    Returns:
        str: The JSON representation of my_obj if possible.
    """
    return (json.dumps(my_obj))
