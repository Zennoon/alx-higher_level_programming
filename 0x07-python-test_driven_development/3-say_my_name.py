#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-say_my_name

Author: Yunus Kedir

This module holds a function, say_my_name, which has tests implemented
in the 3-say_my_name.txt file in the tests directory. The tests are in
the docstring and are executed by the doctest module.

"""


def say_my_name(first_name, last_name=""):
    if first_name.__class__ is not str:
        raise TypeError("first_name must be a string")
    if last_name.__class__ is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
