#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" test_base.py

Author: Yunus Kedir

This module contains:

Classes:
    TestBase - Contains unittest tests for the models/base.py module

"""


import unittest
import models.base as base


Base = base.Base


class TestBase(unittest.TestCase):
    """unittest test cases for the models/base.py module."""
    def test_valid_module(self):
        """Tests that the imported module is valid."""
        self.assertEqual(base.__class__.__name__, "module")

    def test_valid_class(self):
        """Tests that the imported module contains the valid class."""
        self.assertEqual(Base.__class__.__name__, "type")
        b = Base()
        self.assertIsInstance(b, Base)

    def test_incorrect_num_args(self):
        """Tests the class when an incorrect num of args is passes to init."""
        with self.assertRaises(TypeError):
            b = Base(1, "Too many args")

    def test_id_value(self):
        """Tests the Base class with a valid id value passed to __init__."""
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(10)
        self.assertEqual(b.id, 10)
        b = Base(-10)
        self.assertEqual(b.id, -10)

    def test_id_None(self):
        """Tests the Base class with default id value (None)."""
        for i in range(5):
            with self.subTest(i=i):
                b = Base()
                self.assertEqual(b.id, Base.__dict__["_Base__nb_objects"])
        b = Base(None)
        self.assertEqual(b.id, Base.__dict__["_Base__nb_objects"])

    def test_mix(self):
        """Tests the Base class when there is a mix of instances with given
        id value and default id value."""
        b = Base(50)
        self.assertEqual(b.id, 50)
        b = Base()
        self.assertEqual(b.id, Base.__dict__["_Base__nb_objects"])
        b = Base(49)
        self.assertEqual(b.id, 49)

    def test_non_int_id(self):
        """Tests the Base class with non-integer id values passed."""
        b = Base('5')
        self.assertEqual(b.id, '5')
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base(True)
        self.assertEqual(b.id, True)
        b = Base(1 + 2j)
        self.assertEqual(b.id, 1 + 2j)

    def test_private_attribute(self):
        """Tests that the __nb_objects class attribute is private."""
        b = Base()
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_change_id(self):
        """Tests the behavior when id of an instance is changed."""
        b = Base(1)
        self.assertEqual(b.id, 1)
        b.id = 5
        self.assertEqual(b.id, 5)

    def test_to_json_string_method(self):
        """Tests the to_json_string method of the Base class."""
        b = Base()
        self.assertEqual(b.to_json_string(None), '[]')
        self.assertEqual(b.to_json_string([]), '[]')
        self.assertEqual(b.to_json_string("Not a dict"), '"Not a dict"')
        self.assertEqual(b.to_json_string(1.5), '1.5')
        self.assertEqual(b.to_json_string([{'x': 1, 'y': 2}]),
                         '[{"x": 1, "y": 2}]')

    def test_from_json_string(self):
        """Tests the from_json_string method of the Base class."""
        b = Base()
        self.assertEqual(b.from_json_string(None), [])
        self.assertEqual(b.from_json_string(""), [])
        self.assertEqual(b.from_json_string('[]'), [])
        self.assertEqual(b.from_json_string('"A string"'), "A string")
        self.assertEqual(b.from_json_string('[{"x": 1, "y": 2}]'),
                         [{"x": 1, "y": 2}])
