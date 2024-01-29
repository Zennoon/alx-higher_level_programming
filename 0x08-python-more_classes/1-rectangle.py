#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-rectangle.py

Author: Yunus Kedir

This module creates the Rectangle class object (like the 0-rectangle module)
with new private attributes.
"""


class Rectangle(object):
    """A class that represents a Rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initializes newly created Rectangle objects with width and height
        attribute.

        Args:
            width (int): Width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter and setter property pair for the private width attribute.

        The setter performs width validation.
        1. width must be an integer
        2. width must be >= 0
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
        1. height must be an integer
        2. height must be >= 0
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if value.__class__ is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
