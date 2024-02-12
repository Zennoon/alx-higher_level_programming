#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" rectangle.py

Author: Yunus Kedir

This module contains:

Classes:
    TestRectangle - Contains unittest tests for the models.square module

"""


import unittest
import sys
import io
import models.square as square
import models.rectangle as rectangle
import models.base as base


Square = square.Square
Rectangle = rectangle.Rectangle
Base = base.Base


class TestSquare(unittest.TestCase):
    """unittest test cases for the models.square module."""
    def setUp(self):
        """Set up fixture for the tests."""
        pass

    def tearDown(self):
        """Tear down fixture for the tests."""
        pass

    def test_valid_module(self):
        """Tests that the module has been imported successfully."""
        self.assertEqual(square.__class__.__name__, "module")

    def test_valid_class(self):
        """Tests that the imported module contains the desired class."""
        self.assertEqual(Square.__class__.__name__, "type")
        s = Square(1, 1)
        self.assertIsInstance(s, Square)

    def test_inheritance(self):
        """Tests that the Square class inherits from the Rectangle and
        Base classes."""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_incorrect_num_args(self):
        """Tests the class when an incorrect num of args is passed to init."""
        # The width and height args are mandatory.
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(10, 0, 0, 99, "Too many args")

    def test_private_attributes(self):
        """Tests that the instance attributes are private."""
        s = Square(10)
        with self.assertRaises(AttributeError):
            print(s.__width)
        with self.assertRaises(AttributeError):
            print(s.__height)
        with self.assertRaises(AttributeError):
            print(s.__x)
        with self.assertRaises(AttributeError):
            print(s.__y)

    def test_size_attr(self):
        """Tests the getter and setter (and its validation) of the size
        attribute."""
        s = Square(10)
        self.assertEqual(s.width, 10)
        s.width = s.width * 2
        self.assertEqual(s.width, 20)
        for wrong_type in [1.0, 1 + 1j, "1", [1], {}]:
            with self.assertRaises(TypeError):
                s = Square(wrong_type, 1, 1, 1)
            with self.assertRaises(TypeError):
                s = Square(1, 1, 1)
                s.width = wrong_type
        for wrong_val in [0, -1]:
            with self.assertRaises(ValueError):
                s = Square(wrong_val, 1, 1)
            with self.assertRaises(ValueError):
                s = Square(1, 1, 1)
                s.width = wrong_val

    def test_x_attr(self):
        """Tests the getter and setter (and its validation) of the x
        attribute."""
        s = Square(10)
        self.assertEqual(s.x, 0)
        s.x = 2
        self.assertEqual(s.x, 2)
        s = Square(10, 1, 1)
        self.assertEqual(s.x, 1)
        for wrong_type in [1.0, 1 + 1j, "1", [1], {}]:
            with self.assertRaises(TypeError):
                s = Square(1, wrong_type, 1)
            with self.assertRaises(TypeError):
                s = Square(1, 1, 1)
                s.x = wrong_type
        for wrong_val in [-1, -100]:
            with self.assertRaises(ValueError):
                s = Square(1, wrong_val, 1)
            with self.assertRaises(ValueError):
                s = Square(1, 1, 1)
                s.x = wrong_val

    def test_y_attr(self):
        """Tests the getter and setter (and its validation) of the y
        attribute."""
        s = Square(10)
        self.assertEqual(s.y, 0)
        s.y = 2
        self.assertEqual(s.y, 2)
        s = Square(10, 1, 1)
        self.assertEqual(s.y, 1)
        for wrong_type in [1.0, 1 + 1j, "1", [1], {}]:
            with self.assertRaises(TypeError):
                s = Square(1, 1, wrong_type)
            with self.assertRaises(TypeError):
                s = Square(1, 1, 1)
                s.y = wrong_type
        for wrong_val in [-1, -100]:
            with self.assertRaises(ValueError):
                s = Square(1, 1, wrong_val)
            with self.assertRaises(ValueError):
                s = Square(1, 1, 1)
                s.y = wrong_val

    def test_id(self):
        """Tests the id attribute of the Square instance."""
        s = Square(10, 2, 3, 99)
        self.assertEqual(s.id, 99)
        s = Square(10, 10)
        self.assertEqual(s.id, Base.__dict__["_Base__nb_objects"])
        s.id = 25
        self.assertEqual(s.id, 25)

    def test_area_method(self):
        """Tests the area method of the Square class."""
        s = Square(10, 5, 5)
        self.assertEqual(s.area(), 100)
        s.width = 5
        s.height = 5
        self.assertEqual(s.area(), 25)
        s.width = 2
        s.height = 2
        self.assertEqual(s.area(), 4)
        s.x = 0
        s.y = 0
        self.assertEqual(s.area(), 4)

    def test_display_method(self):
        """Tests the display method of the Square class."""
        # Redirecting sys.stdout to a io object to capture the output
        output = io.StringIO()
        sys.stdout = output
        s = Square(1)
        s.display()
        self.assertEqual(output.getvalue(), "#\n")

        output = io.StringIO()
        sys.stdout = output
        s = Square(3, 0, 0)
        s.display()
        self.assertEqual(output.getvalue(), "###\n###\n###\n")

        output = io.StringIO()
        sys.stdout = output
        s.width = 5
        s.height = 5
        s.display()
        self.assertEqual(output.getvalue(),
                         "#####\n#####\n#####\n#####\n#####\n")

        # Returning sys.stdout to original value
        sys.stdout = sys.__stdout__

    def test_display_method_with_xy(self):
        """Tests the display method when the x, and y values are not 0."""
        output = io.StringIO()
        sys.stdout = output
        s = Square(1, 3, 5)
        s.display()
        self.assertEqual(output.getvalue(), "\n\n\n\n\n   #\n")

        output = io.StringIO()
        sys.stdout = output
        s = Square(3, 2, 1)
        s.display()
        self.assertEqual(output.getvalue(), "\n  ###\n  ###\n  ###\n")

        output = io.StringIO()
        sys.stdout = output
        s.width = 2
        s.height = 2
        s.x = 3
        s.y = 2
        s.display()
        self.assertEqual(output.getvalue(), "\n\n   ##\n   ##\n")

        # Returning sys.stdout to original value
        sys.stdout = sys.__stdout__

    def test_str_method(self):
        """Tests the __str__ method of the Square class."""
        # Redirecting sys.stdout to a io object to capture the output
        output = io.StringIO()
        sys.stdout = output
        s = Square(10)
        self.assertEqual(str(s),
    "[Square] ({}) 0/0 - 10".format(Base.__dict__["_Base__nb_objects"]))
        print(s)
        self.assertEqual(output.getvalue(),
    "[Square] ({}) 0/0 - 10\n".format(Base.__dict__["_Base__nb_objects"]))

        output = io.StringIO()
        sys.stdout = output
        s.width = 12
        s.x = 2
        s.y = 3
        s.id = 98
        self.assertEqual(str(s), "[Square] (98) 2/3 - 12")
        print(s)
        self.assertEqual(output.getvalue(), "[Square] (98) 2/3 - 12\n")

        # Returning sys.stdout to original value
        sys.stdout = sys.__stdout__

    def test_update_method_args(self):
        """Tests the update method of the Rectangle class with *args."""
        s = Square(10)
        s.update()
        self.assertEqual(str(s),
    "[Square] ({}) 0/0 - 10".format(Base.__dict__["_Base__nb_objects"]))
        s.update(0)
        self.assertEqual(str(s), "[Square] (0) 0/0 - 10")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(3, 4, 5)
        self.assertEqual(str(s), "[Square] (3) 0/0 - 4")
        s.update(6, 7, 8, 9)
        self.assertEqual(str(s), "[Square] (6) 9/0 - 7")
        s.update(10, 11, 12, 13, 14)
        self.assertEqual(str(s), "[Square] (10) 13/14 - 11")
        s.update(15, 16, 17, 18, 19, "Extra args ignored")
        self.assertEqual(str(s), "[Square] (15) 18/19 - 16")

    def test_update_method_kwargs(self):
        s = Square(10)
        s.update(id=100)
        self.assertEqual(str(s), "[Square] (100) 0/0 - 10")
        s.update(width=12, id=25)
        self.assertEqual(str(s), "[Square] (25) 0/0 - 12")
        s.update(height=15, width=6, id=98)
        self.assertEqual(str(s), "[Square] (98) 0/0 - 6")
        s.update(height=15, volume="Doesn't exist", width=6, id=98, z='z')
        self.assertEqual(str(s), "[Square] (98) 0/0 - 6")
        s.update(x=20, width=6, id=8, y=7, height=21)
        self.assertEqual(str(s), "[Square] (8) 20/7 - 6")
        s.update(x=20, width=6, id=9, y=7, height=21)
        self.assertEqual(str(s), "[Square] (9) 20/7 - 6")
        # kwargs ignored if args exists and not None
        s.update(1, x=2, width=3, id=4, y=5, height=6)
        self.assertEqual(str(s), "[Square] (1) 20/7 - 6")
        # Invalid types & vals ignored because kwargs is shadowed by args
        s.update(0, x="wrong", width=-5, id=False, y=1.5, height={})
        self.assertEqual(str(s), "[Square] (0) 20/7 - 6")

    def test_update_method_type_validation(self):
        """Tests that the attrs type validation works on update."""
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.update(98, '1')
        with self.assertRaises(TypeError):
            s.update(98, 1, '2')
        with self.assertRaises(TypeError):
            s.update(98, 1, 2, '3')
        with self.assertRaises(TypeError):
            s.update(98, 1, 2, 3, '4')
        with self.assertRaises(TypeError):
            s.update(id=98, width='1')
        with self.assertRaises(TypeError):
            s.update(height=(1 + 2j), width=2)
        with self.assertRaises(TypeError):
            s.update(width=1, id=5, x=[0])
        with self.assertRaises(TypeError):
            s.update(y={98}, width=1, x=2, height=3, id=25)

    def test_update_method_value_validation(self):
        """Tests that the attrs value validation still works on update."""
        s = Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            s.update(98, 0)
        with self.assertRaises(ValueError):
            s.update(98, 1, 0)
        with self.assertRaises(ValueError):
            s.update(98, 1, 2, -1)
        with self.assertRaises(ValueError):
            s.update(98, 1, 2, 3, -1)
        with self.assertRaises(ValueError):
            s.update(id=98, width=0)
        with self.assertRaises(ValueError):
            s.update(id=98, height=0, width=15)
        with self.assertRaises(ValueError):
            s.update(x=-1, width=1, height=2, id=-1)
        with self.assertRaises(ValueError):
            s.update(x=98, height=1, id=2, width=3, y=-1)
