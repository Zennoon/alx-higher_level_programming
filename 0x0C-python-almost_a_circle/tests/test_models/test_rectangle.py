#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" rectangle.py

Author: Yunus Kedir

This module contains:

Classes:
    TestRectangle - Contains unittest tests for the models.rectangle module

"""


import unittest
import models.rectangle as rectangle
import models.base as base


Rectangle = rectangle.Rectangle
Base = base.Base


class TestRectangle(unittest.TestCase):
    """unittest test cases for the models.rectangle module."""
    def test_valid_module(self):
        """Tests that the module has been imported successfully."""
        self.assertEqual(rectangle.__class__.__name__, "module")

    def test_valid_class(self):
        """Tests that the imported module contains the desired class."""
        self.assertEqual(Rectangle.__class__.__name__, "type")
        r = Rectangle(1, 1)
        self.assertIsInstance(r, Rectangle)

    def test_inheritance(self):
        """Tests that the Rectangle class inherits from the Base class."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_incorrect_num_args(self):
        """Tests the class when an incorrect num of args is passed to init."""
        # The width and height args are mandatory.
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(10)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, 0, 0, 99, "Too many args")

    def test_private_attributes(self):
        """Tests that the instance attributes are private."""
        r = Rectangle(10, 10, 1, 1)
        with self.assertRaises(AttributeError):
            print(r.__width)
        with self.assertRaises(AttributeError):
            print(r.__height)
        with self.assertRaises(AttributeError):
            print(r.__x)
        with self.assertRaises(AttributeError):
            print(r.__y)

    def test_width(self):
        """Tests the getter and setter of the width attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.width, 10)
        r.width = r.width * 2
        self.assertEqual(r.width, 20)

    def test_height(self):
        """Tests the getter and setter of the height attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.height, 10)
        r.height = r.height / 2
        self.assertEqual(r.height, 5)

    def test_x_coord(self):
        """Tests the getter and setter of the x attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.x, 0)
        r.x = 2
        self.assertEqual(r.x, 2)

    def test_y_coord(self):
        """Tests the getter and setter of the y attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.y, 0)
        r.y = 3
        self.assertEqual(r.y, 3)

    def test_id(self):
        """Tests the id attribute of the Rectangle instance."""
        r = Rectangle(10, 10, 2, 3, 99)
        self.assertEqual(r.id, 99)
        r = Rectangle(10, 10)
        self.assertEqual(r.id, Base.__dict__["_Base__nb_objects"])
        r.id = 25
        self.assertEqual(r.id, 25)
