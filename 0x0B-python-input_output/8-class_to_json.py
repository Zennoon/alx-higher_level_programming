#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""8-class_to_json.py

Author: Yunus Kedir

This module contains:

Functions:
    class_to_json - Returns dictionary description of an object to be used for
                    JSON serialization

"""


def class_to_json(obj):
    """Returns a dictionary description of the given object that can be used
    for its JSON serialization.

    The dictionary is a key : value pair of the object's attributes and their
    values.

    Args:
        obj: The object whose description is returned.

    Returns:
        dict: A dictionary that holds obj's attributes and their values.
    """
    return (obj.__dict__)
