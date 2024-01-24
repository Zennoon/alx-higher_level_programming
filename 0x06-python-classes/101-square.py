#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-square.py

Author: Yunus Kedir

This module continues adding further attributes to the Square module from the
5-square module. This time, it introduces a new private field, along with a
getter setter pair for it, it also does some modifications on the my_print
method

"""


class Square(object):
    """Represents a square with some size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a newly created instance of the Square class.

        Args:
            size (int): Size of the square (length of any single side)
            position (tuple): Position of the square in a 2D axis

        self.size = size
        self.position = position

        """
        self.size = size
        self.position = position


    def __str__(self):
        """Returns user-friendly string representation of a Square instance."""
        output = ""
        if self.__size == 0:
            output += '\n'
        else:
            for i in range(self.__position[1]):
                output += '\n'
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    output += ' '
                for k in range(self.__size):
                    output += '#'
                output += '\n'
        return (output[:-1])

    @property
    def size(self):
        """Getter setter pair for the private size attribute.

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

    @property
    def position(self):
        """Getter setter pair for the private position attribute.

        The setter also performs type and value validation for the given
        position.
        """
        return (self.__position)

    @position.setter
    def position(self, tpl):
        if (tpl.__class__ != tuple or len(tpl) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (tpl[0].__class__ != int or tpl[1].__class__ != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (tpl[0] < 0 or tpl[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = tpl

    def area(self):
        """Computes and returns the area of the Square instance.

        Returns:
            int: The area of the Square instance/object.

        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square as a collection of '#' characters.

        The position of the square is considered to be on a 2D plane, with the
        1st element of the position tuple being the x offset from the origin,
        represented by spaces in the printing, and the 2nd element of the tuple
        signifying the y offset of the square from the origin, represented by
        blank lines in the printing.

        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
