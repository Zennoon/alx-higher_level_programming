#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-square.py

Author: Yunus Kedir

This module builds on the Square class from the 3-square module by creating
getter and setter functions or rather using decorators to access and manipulate
the private size instance attribute

"""


class Square(object):
    """Represents a square with some size."""

    def __init__(self, size=0):
        """Initializes newly created Square instances/objects.

        Args:
            size (int): The size of the square (size of a single side)

        """
        self.size = size

    @property
    def size(self):
        """Getter and setter pair for the private size attribute.

        The setter also does type and value validation for the given size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if value.__class__ != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes and returns the area of the Square instance.

        Returns:
            The area of the Square instance/object.

        """
        return (self.__size ** 2)
