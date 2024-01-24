#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""103-magic_class.py

Author: Yunus Kedir

This script was created to create python code or a class to be specific, that
would generate the same bytecode as the one given in the task.

"""
from dis import dis


class MagicClass:
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return (2 * math.pi * self.__radius)
