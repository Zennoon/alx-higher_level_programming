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
