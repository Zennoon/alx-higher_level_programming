#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-my_list.py

Author: Yunus Kedir

This module contains a class that inherits from the list class, and has one
additional method defined. The tests for this module can be found in the
tests directory inside 1-my_list.txt

"""


class MyList(list):
    """A custom class for lists, but with a method to print the list sorted."""
    def print_sorted(self):
        """Prints the list (or its representation) in an ascending order."""
        print(sorted(self))
