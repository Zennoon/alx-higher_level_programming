#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5-rectangle.py

Author: Yunus Kedir

This module adds on to the Rectangle class of the 4-rectangle module by adding
the magic method __del__ that imitates a destructor of an instance. It is
called when all the references to the instance have been deleted (reference
count is 0) and python's garbage collector is about to reclaim the memory
held by the instance.
"""


class Rectangle(object):
    """A class that represents a rectangle with given width and height."""
    def __init__(self, width=0, height=0):
        """Initializes a newly created Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def __del__(self):
        """Executed when an instance is garbage collected."""
        print("Bye rectangle...")

    def __str__(self):
        """Returns an informal string representation of the calling instance.

        Returns:
            (str): It returns the rectangle made with '#' characters.
        """
        output = ""
        for i in range(self.area()):
            if i and i % self.__width == 0:
                output += '\n'
            output += '#'
        return (output)

    def __repr__(self):
        """Returns a formal string representation of the calling instance.

        Returns:
            (str): String that can be passed to eval to create a new instance.
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    @property
    def width(self):
        """Getter and setter property pair for the private width attribute.

        The setter performs width validation.
        1. width must be an integer.
        2. width must be >= 0.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if value.__class__ is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter property pair for the private height attribute.

        The setter performs height validation.
        1. height must be an integer.
        2. height must be >= 0.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if value.__class__ is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of a Rectangle instance.

        Returns:
            (int): Area of self.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and returns the perimeter of a Rectangle instance.

        If either width or heigth of the instance is 0, the perimeter is
        returned as 0.

        Returns:
            (int): Perimeter of self
        """
        if self.__width and self.__height:
            return ((2 * self.__width) + (2 * self.__height))
        return (0)
