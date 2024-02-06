#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""10-student.py

Author: Yunus Kedir

This module contains:

Classes:
    Student - Ordinary class with a method that returns an instance's
              dictionary representation of selected attributes, and a
              method for replacing the attributes of an instance using
              another dictionary.

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

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the calling instance that
        only includes the attribute names found in a given list if it is valid.

        Args:
            attrs (list<str>): A list of attribute names to include in the
            returned dictionary.

        Returns:
            dict: A dictionary of the attributes of the instance that are in
                  attrs if it is a valid list of strings.
        """
        if attrs is not None:
            dict_repr = {}
            for attr in attrs:
                if self.__dict__.get(attr):
                    dict_repr[attr] = self.__dict__.get(attr)
            return (dict_repr)
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces the attributes of calling instances with the values in
        a given dictionary.

        Args:
            json: The dictionary to replace from.
        """
        if json is not None:
            for key in json.keys():
                if self.__dict__.get(key) is not None:
                    self.__dict__[key] = json[key]
