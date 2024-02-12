#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" rectangle.py

Author: Yunus Kedir

This module contains:

Classes:
    Rectangle - Inherits from Base and has width and height

"""


from models.base import Base


class Rectangle(Base):
    """Represents a rectangle with a width and height property."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a newly created Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle in a 2D plane.
            y (int): Y-coordinate of the rectangle in a 2D plane.
            id (int): ID of the instance.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Magic method to handle the print and str functions on an instance."""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id,
                                                 self.__x, self.__y,
                                                 self.__width, self.__height))

    @property
    def width(self):
        """Getter and setter pair for the width private instance attribute."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if value.__class__ is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter pair for the height private instance attribute."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if value.__class__ is not int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter and setter pair for the x private instance attribute."""
        return (self.__x)

    @x.setter
    def x(self, value):
        if value.__class__ is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter and setter pair for the y private instance attribute."""
        return (self.__y)

    @y.setter
    def y(self, value):
        if value.__class__ is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """Prints the Rectangle with the '#' character."""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)
