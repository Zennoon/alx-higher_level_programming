#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-max_integer.py

Author: Yunus Kedir

This module contains a function that returns the maximum integer in a list
of integers. The function has intentionally been implemented without much
type checking. This is done to experiment with the tests in
tests/6-max_integer_test.py that have been developed with the unittest module.

"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.

    If the list is empty, the function returns None.

    Args:
        list (list<int>): The list whose max integer element is returned.
    """
    if len(list) == 0:
        return (None)
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return (result)
