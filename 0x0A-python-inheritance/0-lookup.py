#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-lookup.py

Author: Yunus Kedir

This module contains a function that can be used to get a list of the available
attributes (fields + methods) that an object has available.

"""


def lookup(obj):
    """Returns a list of all available attributes of a given object.

    Args:
        obj: An arbitrary object.

    Returns:
        list<str>: A list of the attributes of obj (empty list if obj == None).
    """
    return (dir(obj))
