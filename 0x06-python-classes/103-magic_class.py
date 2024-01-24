#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""103-magic_class.py

Author: Yunus Kedir

This script was created to create python code or a class to be specific, that
would generate the same bytecode as the one given in the task.

"""


class MagicClass:
    """The class to implement to imitate the bytecode. Reps a Circle"""
    def __init__(self, radius):
        """Initializes a newly created MagicClass instance.

        Args:
            radius: The radius of the circle, can be int or float
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of an instance."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates and returns the circumference of an instance."""
        return (2 * math.pi * self.__radius)
