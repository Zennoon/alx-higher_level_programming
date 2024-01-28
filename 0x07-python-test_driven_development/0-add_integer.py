#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 0-add_integer

Author: Yunus Kedir

This module contains a function that receives two ints and returns their sum

"""


def add_integer(a, b=98):
    """Validates integer arguments and returns their sum.

    Args:
        a (int): First operand
        b (int): Second operand

    Returns:
        int: a + b

    """
    if a.__class__ not in [int, float]:
        raise TypeError("a must be an integer")
    if b.__class__ not in [int, float]:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
