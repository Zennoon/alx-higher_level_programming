#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-lookup.py

Author: Yunus Kedir

This module contains a function that can be used to get a list of the available
attributes (fields + methods) that an object has available.

"""


def lookup(obj):
    """Returns a list of all available attributes of a given object.

    It uses the built in dir() method that returns a list of the attributes
    (fields and methods) including the special attributes like __class__ of
    an object.

    Args:
        obj: An arbitrary object.

    Returns:
        list<str>: A list of all the attributes of obj.
    """
    return (dir(obj))
