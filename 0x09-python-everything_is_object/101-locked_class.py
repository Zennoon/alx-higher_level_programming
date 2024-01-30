#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-locked_class.py

Author: Yunus Kedir

This module contains an empty class that has a __slots__ list preventing the
creation of any dynamically created instance attributes (created after the
instance creation) except those whose name are in the list.
"""


class LockedClass(object):
    """Empty class with a __slots__ list listing the only possible attributes
    to create for an instance of the class."""
    __slots__ = ["first_name"]
