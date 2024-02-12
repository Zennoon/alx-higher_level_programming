#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" rectangle.py

Author: Yunus Kedir

This module contains:

Classes:
    TestRectangle - Contains unittest tests for the models.rectangle module

"""


import unittest
import sys
import io
import json
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
        # Redirecting sys.stdout to a io object to capture the output
        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(1, 1)
        r.display()
        self.assertEqual(output.getvalue(), "#\n")

        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(3, 4, 0, 0)
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

    def test_display_method_with_xy(self):
        """Tests the display method when the x, and y values are not 0."""
        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(1, 1, 3, 5)
        r.display()
        self.assertEqual(output.getvalue(), "\n\n\n\n\n   #\n")

        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(3, 4, 2, 1)
        r.display()
        self.assertEqual(output.getvalue(), "\n  ###\n  ###\n  ###\n  ###\n")

        output = io.StringIO()
        sys.stdout = output
        r.width = 2
        r.height = 3
        r.x = 3
        r.y = 2
        r.display()
        self.assertEqual(output.getvalue(), "\n\n   ##\n   ##\n   ##\n")

        # Returning sys.stdout to original value
        sys.stdout = sys.__stdout__

    def test_str_method(self):
        """Tests the __str__ method of the Rectangle class."""
        # Redirecting sys.stdout to a io object to capture the output
        output = io.StringIO()
        sys.stdout = output
        r = Rectangle(10, 10)
        s = "[Rectangle] ({}) ".format(Base.__dict__["_Base__nb_objects"])
        self.assertEqual(str(r), s + "0/0 - 10/10")
        print(r)
        s = "[Rectangle] ({}) ".format(Base.__dict__["_Base__nb_objects"])
        self.assertEqual(output.getvalue(), s + "0/0 - 10/10\n")

        output = io.StringIO()
        sys.stdout = output
        r.width = 12
        r.height = r.height // 2
        r.x = 2
        r.y = 3
        r.id = 98
        self.assertEqual(str(r), "[Rectangle] (98) 2/3 - 12/5")
        print(r)
        self.assertEqual(output.getvalue(), "[Rectangle] (98) 2/3 - 12/5\n")

        # Returning sys.stdout to original value
        sys.stdout = sys.__stdout__

    def test_update_method_args(self):
        """Tests the update method of the Rectangle class with *args."""
        r = Rectangle(10, 10)
        r.update()
        s = "[Rectangle] ({}) ".format(Base.__dict__["_Base__nb_objects"])
        self.assertEqual(str(r), s + "0/0 - 10/10")
        r.update(0)
        self.assertEqual(str(r), "[Rectangle] (0) 0/0 - 10/10")
        r.update(1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 2/10")
        r.update(3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (3) 0/0 - 4/5")
        r.update(6, 7, 8, 9)
        self.assertEqual(str(r), "[Rectangle] (6) 9/0 - 7/8")
        r.update(10, 11, 12, 13, 14)
        self.assertEqual(str(r), "[Rectangle] (10) 13/14 - 11/12")
        r.update(15, 16, 17, 18, 19, "Extra args ignored")
        self.assertEqual(str(r), "[Rectangle] (15) 18/19 - 16/17")

    def test_update_method_kwargs(self):
        """Tests the update method of the Rectangle class with *kwargs."""
        r = Rectangle(10, 10)
        r.update(id=100)
        self.assertEqual(str(r), "[Rectangle] (100) 0/0 - 10/10")
        r.update(width=12, id=25)
        self.assertEqual(str(r), "[Rectangle] (25) 0/0 - 12/10")
        r.update(height=15, width=6, id=98)
        self.assertEqual(str(r), "[Rectangle] (98) 0/0 - 6/15")
        r.update(height=15, volume="Doesn't exist", width=6, id=98, z='z')
        self.assertEqual(str(r), "[Rectangle] (98) 0/0 - 6/15")
        r.update(x=20, width=6, id=8, y=7, height=21)
        self.assertEqual(str(r), "[Rectangle] (8) 20/7 - 6/21")
        r.update(x=20, width=6, id=8, y=7, height=21)
        self.assertEqual(str(r), "[Rectangle] (8) 20/7 - 6/21")
        # kwargs ignored if args exists and not None
        r.update(1, x=2, width=3, id=4, y=5, height=6)
        self.assertEqual(str(r), "[Rectangle] (1) 20/7 - 6/21")
        # Invalid types ignored because kwargs is shadowed by args
        r.update(0, x="wrong", width=[5], id=False, y=1.5, height={})
        self.assertEqual(str(r), "[Rectangle] (0) 20/7 - 6/21")

    def test_update_method_type_validation(self):
        """Tests that the attrs type validation works on update."""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.update(98, '1')
        with self.assertRaises(TypeError):
            r.update(98, 1, '2')
        with self.assertRaises(TypeError):
            r.update(98, 1, 2, '3')
        with self.assertRaises(TypeError):
            r.update(98, 1, 2, 3, '4')
        with self.assertRaises(TypeError):
            r.update(id=98, width='1')
        with self.assertRaises(TypeError):
            r.update(height=(1 + 2j), width=2)
        with self.assertRaises(TypeError):
            r.update(width=1, id=5, x=[0])
        with self.assertRaises(TypeError):
            r.update(y={98}, width=1, x=2, height=3, id=25)

    def test_update_method_value_validation(self):
        """Tests that the attrs value validation still works on update."""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r.update(98, 0)
        with self.assertRaises(ValueError):
            r.update(98, 1, 0)
        with self.assertRaises(ValueError):
            r.update(98, 1, 2, -1)
        with self.assertRaises(ValueError):
            r.update(98, 1, 2, 3, -1)
        with self.assertRaises(ValueError):
            r.update(id=98, width=0)
        with self.assertRaises(ValueError):
            r.update(id=98, height=0, width=15)
        with self.assertRaises(ValueError):
            r.update(x=-1, width=1, height=2, id=-1)
        with self.assertRaises(ValueError):
            r.update(x=98, height=1, id=2, width=3, y=-1)

    def test_to_dictionary_method(self):
        """Tests the to_dictionary method of the Rectangle class."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(r.to_dictionary(), dict)
        self.assertEqual(r.to_dictionary(), {
            'x': 3,
            'y': 4,
            "width": 1,
            "height": 2,
            "id": 5
        }
        )
        r2 = Rectangle(5, 5)
        self.assertEqual(r2.to_dictionary(), {
            'x': 0,
            'y': 0,
            "width": 5,
            "height": 5,
            "id": r2.id
        }
        )
        r2.width = 10
        self.assertEqual(r2.to_dictionary(), {
            'x': 0,
            'y': 0,
            "width": 10,
            "height": 5,
            "id": r2.id
        }
        )
        dct = r.to_dictionary()
        r2.update(**dct)
        self.assertEqual(r2.to_dictionary(), dct)
        self.assertIsNot(r, r2)

    def test_to_json_string_method(self):
        """Tests the to_json_string method of the Base class."""
        self.assertEqual(Rectangle.to_json_string(None), '[]')
        self.assertEqual(Rectangle.to_json_string([]), '[]')
        r = Rectangle(10, 10)
        dct = r.to_dictionary()
        json_str = r.to_json_string([dct])
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, json.dumps([dct], sort_keys=True))

    def test_save_to_file_method(self):
        """Tests the save_to_file method of the Base class."""
        r = Rectangle(10, 10)
        r2 = Rectangle(1, 2, 3, 4, 5)
        json_str = r.to_json_string([r.to_dictionary(), r2.to_dictionary()])
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", 'r', encoding="utf-8") as f:
            self.assertEqual(json_str, f.read())
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r', encoding="utf-8") as f:
            self.assertEqual('[]', f.read())
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r', encoding="utf-8") as f:
            self.assertEqual('[]', f.read())
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("string")
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([1, 2, 3, 4])

    def test_from_json_string(self):
        """Tests the from_json_string method of the Base class."""
        r = Rectangle(10, 10)
        json_str = r.to_json_string([r.to_dictionary()])
        self.assertEqual(r.from_json_string(json_str), [r.to_dictionary()])

    def test_create_method(self):
        """Tests the create method of the Base class."""
        r = Rectangle(10, 10)
        dct = r.to_dictionary()
        r2 = Rectangle.create(**dct)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r.to_dictionary(), r2.to_dictionary())
        with self.assertRaises(TypeError):
            Rectangle.create(None)

    def test_load_from_file_method(self):
        """Tests the load_from_file method of the Base class."""
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
        r = Rectangle(10, 10)
        r2 = Rectangle(5, 6)
        r3 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r, r2, r3])
        old_rs = [r, r2, r3]
        new_rs = Rectangle.load_from_file()
        for idx, rect in enumerate(new_rs):
            self.assertIsInstance(rect, Rectangle)
            self.assertEqual(rect.to_dictionary(), old_rs[idx].to_dictionary())

    def test_save_to_file_csv_load_from_file_csv_method(self):
        """Tests the save_to_file_csv and load_from_file_csv methods of
        the Base class."""
        Rectangle.save_to_file_csv(None)
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        Rectangle.save_to_file_csv([])
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        r = Rectangle(10, 10)
        r2 = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file_csv([r, r2])
        r3, r4 = Rectangle.load_from_file_csv()
        self.assertIsInstance(r3, Rectangle)
        self.assertIsInstance(r4, Rectangle)
        self.assertEqual(r.to_dictionary(), r3.to_dictionary())
        self.assertEqual(r2.to_dictionary(), r4.to_dictionary())
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("string")
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([1, 2, 3, 4])
