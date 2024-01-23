#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5.square.py

Author: Yunus Kedir

This adds another method on top of the Square class in the 4-square module.
This new method prints the area of the square using '#'

"""


class Square(object):
    """Represents a square with some size."""

    def __init__(self, size=0):
        """Initializes newly created instances of the Square class.

        Args:
            size (int): The size of the square (length of any single side)

        """
        self.size = size

    @property
    def size(self):
        """Getter and setter pair for the private size field.

        The setter also performs type and value validation of the given size.
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
            int: Area of the square instance/object

        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square as '#' characters to stdout."""

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
