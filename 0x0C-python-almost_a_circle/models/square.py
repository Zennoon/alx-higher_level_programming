#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" square.py

Author: Yunus Kedir

This module contains:

Classes:
    Square - Child class of Rectangle, represents a square (special rectangle)

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from the Rectangle class.

    A square is just a rectangle where width = height.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a newly created Square instance.

        It uses the parent class's init method to initialize.

        Args:
            size (int): Width and height of the square.
            x (int): X-coordinate of the square in a 2D plane.
            y (int): Y-coordinate of the square in a 2D plane.
            id (int): ID of the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Magic method to handle the print and str functions on an instance."""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                            self.id, self.x, self.y,
                                            self.width))

    @property
    def size(self):
        """Getter and setter for the width and height attributes."""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the attributes.

        Args:
            args (tuple): Tuple of values to change the attributes to.
                          1st argument should be the id attribute
                          2nd argument should be the size attribute
                          3rd argument should be the x attribute
                          4th argument should be the y attribute

            kwargs (dict): Dict of key - value pairs representing attribute
                           names and values to change them to.
        """
        if args is None or len(args) == 0:
            if kwargs is not None:
                if kwargs.get("id") is not None:
                    self.id = kwargs["id"]
                if kwargs.get("size") is not None:
                    self.size = kwargs["size"]
                if kwargs.get("x") is not None:
                    self.x = kwargs["x"]
                if kwargs.get("y") is not None:
                    self.y = kwargs["y"]
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
