#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-inherits_from.py

Author: Yunus Kedir

This module contains:

Functions:
    inherits_from - Checks if a given object is an instance of a class that
                    inherits from a given class. (Same class is not valid)
"""


def inherits_from(obj, a_class):
    """Returns True if a given object is an instance of a class that inherits
    from a given class.

    Args:
        obj: An arbitrary object whose class is checked.
        a_class: Name of a class which is checked against obj's class for
                 inheritance.

    Returns:
        bool: True if obj is an instance of a class that inherits from a_class
              False otherwise.
    """
    return (isinstance(obj, a_class) and obj.__class__ is not a_class)
