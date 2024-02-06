#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""9-student.py

Author: Yunus Kedir

This module contains:

Classes:
    Student - Ordinary class with a method that returns an instance's
              dictionary representation

"""


class Student(object):
    """Simple class that represents a student with basic attributes."""
    def __init__(self, first_name, last_name, age):
        """Initiates a newly created Student instance.

        Args:
            first_name (str): First name of the student instance.
            last_name (str): Last name of the student instance.
            Age (int): Age of the student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the calling instance."""
        return (self.__dict__)
