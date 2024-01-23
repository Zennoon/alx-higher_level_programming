#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-square.py

This module is a continuation of the 1-square module having value validation
for the size attribute of the Square instances

"""


class Square(object):
    """Represents a Square with a given size."""

    def __init__(self, size=0):
        """Initializer for newly created Square instances.

        Args:
            size (int): Size of the square (length of a single side)

        """
        if size.__class__ != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
