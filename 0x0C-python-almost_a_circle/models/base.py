#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" base.py

Author: Yunus Kedir

This module contains:

Classes:
    Base: Base class for other classes of the project

"""


class Base(object):
    """Base class for all other classes in the project."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes a newly created Base instance.

        Args:
            id (int): ID of the Base instance. If not None, assigned to the
                      object's public attribute 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
