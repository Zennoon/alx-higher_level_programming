#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-max_integer_test.py

Author: Yunus Kedir

This module contains unittest tests for the function max_integer which
can be found in the 6-max_integer.py module in the parent directory.

"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class Test_max_integer(unittest.TestCase):
    """The testing class for the max_integer function.

    It inherits from the TestCase class in the unittest module.
    """

    def test_valid_args(self):
        """Tests the function with valid arguments (a list  of integers)."""

        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_other_types_in_list(self):
        """Tests the function with a list that contains elements other than
        ints, but are still comparable to eachother."""

        self.assertEqual(max_integer([1.5, 1.6, 1.7]), 1.7)
        self.assertEqual(max_integer([1, 1.5, 2.0]), 2.0)
        # comparison based on Unicode values of characters (one char at a time)
        self.assertEqual(max_integer(['D', '5', 'a']), 'a')
        self.assertEqual(max_integer(['a', '5000', 'CAPS']), 'a')
        # comparison based on the values of the corresponding elements.
        # The first differing elements decide which is greater.
        # If all corresponding elems are equal, longer list is greater.
        # Otherwise they are equal.
        self.assertEqual(max_integer([[1, 2, 3], [1, 3, 2]]), [1, 3, 2])
        self.assertEqual(max_integer([['A', 'B', 'C'], ['a']]), ['a'])
        self.assertEqual(max_integer([(1, 2, 3), (2,)]), (2,))
        self.assertEqual(max_integer([{1, 2}, {2, 3}]), {1, 2})

    def test_string_arg(self):
        """Tests the function with strings arguments."""

        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer("1"), '1')
        self.assertEqual(max_integer("Hello World"), 'r')

    def test_tuple_arg(self):
        """Tests the function with tuple arguments."""

        self.assertEqual(max_integer(tuple()), None) # Empty tuple
        self.assertEqual(max_integer((1,)), 1)
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertEqual(max_integer(('1', 'a', 'Z')), 'a')

    def test_dict_arg(self):
        """Tests the function with dict arguments.

        The function works for dict args in only 2 cases.
        1. The dict is empty (has a length of 0)
        2. All the keys are ints starting from 0 and incrementing to len - 1,
        that way, they can be indiced by the function using ints.
        """

        self.assertEqual(max_integer(dict()), None)
        self.assertEqual(max_integer({0: 'a', 1: 'b', 2: 'c'}), 'c')
        self.assertRaises(KeyError, max_integer, {1: 'a', 2: 'b'})
        self.assertRaises(KeyError, max_integer, {0: 'a', 2: 'b'})
        self.assertRaises(KeyError, max_integer, {'a': 0, 'b': 1})

    def test_set_arg(self):
        """Tests the function with set arguments.

        The function works for set args only if the set is empty.
        Otherwise it fails, because sets are not scriptable using ints.
        """

        self.assertEqual(max_integer(set()), None)
        self.assertRaises(TypeError, max_integer, {0, 1, 2, 3})
        self.assertRaises(TypeError, max_integer, {'a', 'b', 'c'})

    def test_incomparable_elems_list(self):
        """Tests the function with lists that contain elements that can't be
        compared to each other."""

        self.assertRaises(TypeError, max_integer, [1, '1'])
        self.assertRaises(TypeError, max_integer, (1, '1'))
        self.assertRaises(TypeError, max_integer, ['1', ['1']])
        self.assertRaises(TypeError, max_integer, [[1], [[1]]])
        self.assertRaises(TypeError, max_integer, [[1, 2], (1, 2)])
        self.assertRaises(TypeError, max_integer, [1, [1], (1,)])
        self.assertRaises(TypeError, max_integer, [1, 1 + 1j])
        self.assertRaises(TypeError, max_integer, [1, {1: 'a'}, (1,)])
        # comparison is not supported between instances of complex.
        self.assertRaises(TypeError, max_integer, [1 + 1j, 1 + 2j])
        # Ordinary relational comparison is not supported between dict instances
        self.assertRaises(TypeError, max_integer, [{'a': 1}, {'b': 2}])
        self.assertRaises(TypeError, max_integer, [[{'a': 1}], [{'b': 2}]])
        self.assertRaises(TypeError, max_integer, [(1, 2), {1, 2}])

    def test_invalid_arg(self):
        """Tests the function with invalid arguments that are not iterable,
        or have no __len__ method."""

        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.5)

    def test_too_many_args(self):
        """Tests the function with too many arguments."""

        self.assertRaises(TypeError, max_integer, [1, 2, 3], True)
