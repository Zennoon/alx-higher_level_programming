#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-square.py

Adds a public method to the square class from 2-square module to compute the
area of the Square instance

"""


class Square(object):
    """Represents a square with some size."""

    def __init__(self, size=0):
        """Initializes newly created Square instances/objects.

        Args:
            size (int): The size of the square (length of a single side)

        """
        if size.__class__ != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes and returns the area of the Square object.

        Returns:
            The area of the Square instance/object.

        """
        return (self.__size ** 2)
