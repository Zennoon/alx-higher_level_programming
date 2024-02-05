#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-is_same_class.py

Author: Yunus Kedir

This module contains a function that returns True if an object is exactly an
instance of a given class and False otherwise.

"""


def is_same_class(obj, a_class):
    """Returns True if an object is a direct instance of a given class
    and False otherwise.

    Args:
        obj: An arbitrary object whose class is checked.
        a_class: A class name to check the class of obj against.
    """
    return (obj.__class__ is a_class)
