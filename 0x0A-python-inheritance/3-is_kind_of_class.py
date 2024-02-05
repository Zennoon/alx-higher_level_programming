#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-is_kind_of_class.py

Author: Yunus Kedir

This module contains a function that checks if a given object is an instance
of a given class or its children classes.

"""


def is_kind_of_class(obj, a_class):
    """Returns True if a given object is either an instance of a given class or
    an instance of its children classes, and returns False Otherwise.

    Args:
        obj: An arbitrary object whose class is checked.
        a_class: Name of a class which is checked against obj.

    Returns:
        bool: True if obj is an instance of a_class or any of its children
              False otherwise.
    """
    return (isinstance(obj, a_class))
