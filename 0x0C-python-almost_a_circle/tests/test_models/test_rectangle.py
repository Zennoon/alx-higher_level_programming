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
    def setUp(self):
        """Set up fixture for the tests."""
        pass

    def tearDown(self):
        """Tear down fixture for the tests."""
        pass

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

    def test_width_attr(self):
        """Tests the getter and setter (and its validation) of the width
        attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.width, 10)
        r.width = r.width * 2
        self.assertEqual(r.width, 20)
        for wrong_type in [1.0, 1 + 1j, "1", [1], {}]:
            with self.assertRaises(TypeError):
                r = Rectangle(wrong_type, 1, 1, 1)
            with self.assertRaises(TypeError):
                r = Rectangle(1, 1, 1, 1)
                r.width = wrong_type
        for wrong_val in [0, -1]:
            with self.assertRaises(ValueError):
                r = Rectangle(wrong_val, 1, 1, 1)
            with self.assertRaises(ValueError):
                r = Rectangle(1, 1, 1, 1)
                r.width = wrong_val

    def test_height_attr(self):
        """Tests the getter and setter (and its validation) of the height
        attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.height, 10)
        r.height = r.height // 2
        self.assertEqual(r.height, 5)
        for wrong_type in [1.0, 1 + 1j, "1", [1], {}]:
            with self.assertRaises(TypeError):
                r = Rectangle(1, wrong_type, 1, 1)
            with self.assertRaises(TypeError):
                r = Rectangle(1, 1, 1, 1)
                r.height = wrong_type
        for wrong_val in [0, -1]:
            with self.assertRaises(ValueError):
                r = Rectangle(1, wrong_val, 1, 1)
            with self.assertRaises(ValueError):
                r = Rectangle(1, 1, 1, 1)
                r.height = wrong_val

    def test_x_attr(self):
        """Tests the getter and setter (and its validation) of the x
        attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.x, 0)
        r.x = 2
        self.assertEqual(r.x, 2)
        r = Rectangle(10, 10, 1, 1)
        self.assertEqual(r.x, 1)
        for wrong_type in [1.0, 1 + 1j, "1", [1], {}]:
            with self.assertRaises(TypeError):
                r = Rectangle(1, 1, wrong_type, 1)
            with self.assertRaises(TypeError):
                r = Rectangle(1, 1, 1, 1)
                r.x = wrong_type
        for wrong_val in [-1, -100]:
            with self.assertRaises(ValueError):
                r = Rectangle(1, 1, wrong_val, 1)
            with self.assertRaises(ValueError):
                r = Rectangle(1, 1, 1, 1)
                r.x = wrong_val

    def test_y_attr(self):
        """Tests the getter and setter (and its validation) of the y
        attribute."""
        r = Rectangle(10, 10)
        self.assertEqual(r.y, 0)
        r.y = 3
        self.assertEqual(r.y, 3)
        r = Rectangle(10, 10, 1, 1)
        self.assertEqual(r.y, 1)
        for wrong_type in [1.0, 1 + 1j, "1", [1], {}]:
            with self.assertRaises(TypeError):
                r = Rectangle(1, 1, 1, wrong_type)
            with self.assertRaises(TypeError):
                r = Rectangle(1, 1, 1, 1)
                r.y = wrong_type
        for wrong_val in [-1, -100]:
            with self.assertRaises(ValueError):
                r = Rectangle(1, 1, 1, wrong_val)
            with self.assertRaises(ValueError):
                r = Rectangle(1, 1, 1, 1)
                r.y = wrong_val

    def test_id(self):
        """Tests the id attribute of the Rectangle instance."""
        r = Rectangle(10, 10, 2, 3, 99)
        self.assertEqual(r.id, 99)
        r = Rectangle(10, 10)
        self.assertEqual(r.id, Base.__dict__["_Base__nb_objects"])
        r.id = 25
        self.assertEqual(r.id, 25)

    def test_area_method(self):
        """Tests the area method of the Rectangle class."""
        r = Rectangle(10, 10, 5, 5)
        self.assertEqual(r.area(), 100)
        r.width = 5
        self.assertEqual(r.area(), 50)
        r.height = 2
        self.assertEqual(r.area(), 10)
        r.x = 0
        r.y = 0
        self.assertEqual(r.area(), 10)

    def test_display_method(self):
        """Tests the display method of the Rectangle class."""
        import sys
        import io

        # Redirecting sys.stdout to a io object to capture the output
        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(1, 1)
        r.display()
        self.assertEqual(output.getvalue(), "#\n")

        output = io.StringIO()
        sys.stdout = output
        r.width = 3
        r.height = 4
        r.display()
        self.assertEqual(output.getvalue(), "###\n###\n###\n###\n")

        output = io.StringIO()
        sys.stdout = output
        r.width = 5
        r.height = 6
        r.display()
        self.assertEqual(output.getvalue(),
                         "#####\n#####\n#####\n#####\n#####\n#####\n")
        # Returning sys.stdout to original value
        sys.stdout = sys.__stdout__
