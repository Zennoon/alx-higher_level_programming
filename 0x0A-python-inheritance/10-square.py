#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""10-square.py

Author: Yunus Kedir

This module contains:

Classes:
    BaseGeometry: base class for other classes, has 2 instance methods for now.
    Rectangle: Inherits from BaseGeometry. Represents a rectangle.
    Square: Inherits from Rectangle. Represents a Square.

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


class Rectangle(BaseGeometry):
    """Represents a rectangle. Inherits from the BaseGeometry class."""
    def __init__(self, width, height):
        """Initiates a newly created Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int):height of the rectangle.

        Both the width and height values are validated using the
        integer_validator function found in the base class.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a user friendly string representation of calling object."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Calculates and returns the area of the calling instance."""
        return (self.__width * self.__height)


class Square(Rectangle):
    """Represents a square. Inherits from the Rectangle class."""
    def __init__(self, size):
        """Initiates a newly created Square instance.

        Args:
            size (int): Size / length of the square (one side of the square).
        """
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns a user friendly string representation of calling object."""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Calculates and returns the area of the calling instance."""
        return (self.__size ** 2)
