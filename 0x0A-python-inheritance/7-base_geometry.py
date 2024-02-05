#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""7-base_geometry.py

Author: Yunus Kedir

This module contains:

Classes:
    BaseGeometry: base class for future tasks, has 2 instance methods for now.

"""


class BaseGeometry(object):
    """A base class for future tasks with subclasses."""
    def area(self):
        """Raises an Exception that it has not been implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the type and value of the given value.

        Args:
            name (str): Name of the value
            value (int): The value to validate
        """
        if value.__class__ is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
