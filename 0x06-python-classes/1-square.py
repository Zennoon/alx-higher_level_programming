#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-square.py

In this module, a class is defined to represent a square. This class will have
one instance variable size.

"""


class Square(object):
    """A class to represent a square with some size.
    """

    def __init__(self, size):
        """Initializer for a new Square instance.

        Args:
            size (int): The size of the square (size of one side)

        """
        self.__size = size
