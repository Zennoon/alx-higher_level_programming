#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""100-my_int.py

This module contains:

Classes:
    MyInt: Custom class that inherits from int but has != and == inverted.

"""


class MyInt(int):
    """Inherits from int but has the != and == operators inverted."""
    def __ne__(self, other):
        """Handles the != comparison operator between two instances, but
        inversely from the typical meaning.

        Args:
            other (int): The other int object to which self is compared to.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return (super().__eq__(other))

    def __eq__(self, other):
        """Handles the == comparison operator between two instances, but
        inversely from the typical meaning.

        Args:
            other (int): The other int object to which self is compared to.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return (super().__ne__(other))
