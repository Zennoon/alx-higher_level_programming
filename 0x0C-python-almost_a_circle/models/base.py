#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" base.py

Author: Yunus Kedir

This module contains:

Classes:
    Base: Base class for other classes of the project

"""


import json
import csv
import turtle


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
        """Returns python object resulting from evaluation of a JSON string.

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves instances of inheritors of the Base class to a file
        in csv format.

        Args:
            list_objs (list): A list of instances of classes that inherit Base.

        """
        with open("{}.csv".format(cls.__name__), 'w', encoding="utf-8") as f:
            csv_writer = csv.writer(f)
            if list_objs is not None:
                for obj in list_objs:
                    dct = obj.to_dictionary()
                    if obj.__class__.__name__ == "Rectangle":
                        csv_writer.writerow([dct["id"], dct["width"],
                                             dct["height"], dct['x'],
                                             dct['y']])
                    elif obj.__class__.__name__ == "Square":
                        csv_writer.writerow([dct["id"], dct["size"],
                                             dct['x'], dct['y']])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances created from csv rows stored in
        a file."""
        objs = []
        with open("{}.csv".format(cls.__name__), 'r', encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                dct = {}
                if len(row) == 5:
                    dct = {
                        "id": row[0],
                        "width": row[1],
                        "height": row[2],
                        'x': row[3],
                        'y': row[4]
                    }
                elif len(row) == 4:
                    dct = {
                        "id": row[0],
                        "size": row[1],
                        'x': row[2],
                        'y': row[3]
                    }
                for key, val in dct.items():
                    dct[key] = int(val)
                objs.append(cls.create(**dct))
        return (objs)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Uses the turtle module to draw squares and rectangles."""
        sum = 0
        turtle.penup()
        turtle.right(180)
        turtle.forward(200)
        turtle.right(180)
        turtle.pendown()
        turtle.color('red')

        for rect in list_rectangles:
            sum += rect.width
            for i in range(2):
                turtle.forward(rect.width * 5)
                turtle.right(90)
                turtle.forward(rect.height * 5)
                turtle.right(90)
            turtle.penup()
            turtle.forward(20)
            turtle.pendown()

        turtle.penup()
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
        turtle.forward(sum)
        turtle.right(180)
        turtle.color('green')
        turtle.pendown()

        for sq in list_squares:
            for i in range(4):
                turtle.forward(sq.size)
                turtle.right(90)
            turtle.penup()
            turtle.forward(20)
            turtle.pendown()
