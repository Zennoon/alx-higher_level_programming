#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" base.py

Author: Yunus Kedir

This module contains:

Classes:
    Base: Base class for other classes of the project

"""


import json


class Base(object):
    """Base class for all other classes in the project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a newly created Base instance.

        Args:
            id (int): ID of the Base instance. If not None, assigned to the
                      object's public attribute 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string repr of a list of dictionaries.

        Args:
            list_dictionaries (list<dict>): A list of dictionaries that
                                            represent an Instance of a Base
                                            inheritor.

        Returns:
            str: JSON representation of the list.
        """
        if list_dictionaries is None:
            return ("[]")
        return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the JSON representation of instances of Base inheritors to
        a file.

        Args:
            list_objs (list): A list of instances of classes that inherit Base.
        """
        lst_dcts = []
        if list_objs is not None:
            for obj in list_objs:
                lst_dcts.append(obj.to_dictionary())

        json_string = cls.to_json_string(lst_dcts)
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns apython object resulting from evaluation of a JSON string.

        Args:
            json_string (str): A json string that represents a python object.

        Returns:
            A python object that is represented by json_string.
        """
        if json_string is None or json_string == "":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the calling class.

        Args:
            dictionary (dict): A dictionary containing attributes and their
                               values to assign to the new instance.

        Return:
            A new instance of the calling class with attribute values extracted
            from the dictionary."""
        instance = cls(10, 10)
        instance.update(**dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances created from a JSON string stored in
        a file."""
        objs = []
        try:
            f = open("{}.json".format(cls.__name__), 'r', encoding="utf-8")
        except Exception:
            return (objs)
        obj_dcts = cls.from_json_string(f.read())
        f.close()
        for dct in obj_dcts:
            objs.append(cls.create(**dct))
        return (objs)
