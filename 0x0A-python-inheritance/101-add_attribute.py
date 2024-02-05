#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-add_attribute.py

This module contains:

Functions:
    add_attribute - Adds a new attribute to an object if possible, raise
                    an error if not.

"""


def add_attribute(obj, attr, val):
    """Adds a new attribute to a given obj if possible, raises error if not.

    All objects that allow dynamic attribute creation would have a __dict__
    attribute. That is where the attributes are stored and accessed.
    Those that prevent it lack this attribute and instead utilize a __slots__
    attribute or another mechanism to disallow dynamic attribute creation
    after an instance has been created.

    Args:
        obj: The object to add the new attribute to.
        attr: The name of the attribute to add.
        val: The value of the added attribute.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = val
