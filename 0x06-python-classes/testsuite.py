#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-square.py

This module is a continuation of the 1-square module having value validation
for the size attribute of the Square instances

"""


class Square(object):
    """Represents a Square with a given size."""

    def __init__(self, size=0):
        """Initializer for newly created Square instances.

        Args:
            size (int): Size of the square (length of a single side)

        """
        if size.__class__ != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

sq1 = Square(3)
print(type(sq1))
print(sq1.__dict__)

sq2 = Square()
print(type(sq2))
print(sq2.__dict__)

try:
    print(sq1.size)
except Exception as e:
    print(e)

try:
    print(sq1.__size)
except Exception as e:
    print(e)

try:
    sq3 = Square("3")
    print(type(sq3))
    print(sq3.__dict__)
except Exception as e:
    print(e)

try:
    sq4 = Square(-89)
    print(type(sq4))
    print(sq4.__dict__)
except Exception as e:
    print(e)
