#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-print_square.py

Author: Yunus Kedir

This module is a continuation of the TDD project. This one contains a function,
print_square that prints a square of given size with the '#' character. Unit
tests have been prepared for the function in the 4-print_square.txt file in the
tests directory using doctest (the tests are embedded in the text).

"""


def print_square(size):
    """Prints a square of given size using the '#' character.

    The function first validates the given size.
    1. size must be an integer.
    2. size must be >= 0.

    Args:
        size (int): The size of the square to be printed.
    """
    if size.__class__ is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
