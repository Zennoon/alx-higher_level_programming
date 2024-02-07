#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""12-pascal_triangle.py

Author: Yunus Kedir

This module contains:

Functions:
    pascal_triangle - Returns a list of lists representing a pascal triangle of
                      given size
    get_pascal_triangle_line - Returns a list representing a single line of the
                               triangle
    combination - Calculates and returns the combination of two given numbers
    factorial - Calculates and returns the factorial of a given number

"""


def factorial(n):
    """Returns the factorial of a given number.

    Args:
        n (int): The number whose factorial is returned.

    Returns:
        int: The factorial of n.
    """
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def combination(n, k):
    """Returns the combination of two given numbers.

    Combination of two numbers n and k is defined as:
        c(n, k) = factorial(n) / (factorial(k) * factorial(n - k))

    Args:
        n (int): Number of elements taken from for the combination.
        k (int): The number of elements taken at a time for a single comb.

    Returns:
        int: The number of combinations that can be formed from n elements
             taken k elements at a time with out repetition.
    """
    return (factorial(n) // (factorial(k) * factorial(n - k)))


def get_pascal_triangle_line(n):
    """Return a list of integers representing a single line of a pascal
    triangle.

    A single line of a pascal triangle is composed of the integers that
    are coefficients in the expansion of a power of a given number.

    For instance, the line for n = 3 is a list of the coefficients in the
    expansion of let's say (x + y) ** (3). This expression expands to
    x**3 + 3(x)(y**2) + 3(y)(x**2) + y**3. The coefficients, which are
    returned as a list by this function are 1, 3, 3, and 1.

    This function uses the binomial theorem which in turn uses combinations
    to obtain the coefficients of expansion of a given power.

    The binomial theorem is as follows:
        if c(x, y) represents combination(x, y)
        (x + y)**n = c(n, 0)(x**n)(y**0) + c(n, 1)(x**(n-1))(y**1) +
                     c(n, 2)(x**(n-2))(y**2) + ... + c(n, n)(x**0)(y**n)

    Based on this theorem, we can get the coefficients by disregarding the
    variables and focusing on the combination part.

    Args:
        n (int): The number for which to return the sequence.

    Returns:
        list<int>: List of the coefficents of expansion of the power of n.
    """
    coeffs = []
    for k in range(n + 1):
        coeffs.append(combination(n, k))
    return (coeffs)


def pascal_triangle(n):
    """Returns a list of list of integers representing the pascal triangle
    of size n.

    The pascal triangle is composed of lists that each have the coefficients
    of expansion of a given power. This power goes from 0 upto n - 1 if n is the
    requested size of the triangle. Therefore, the returned list is of size n.

    Args:
        n (int): The size of the triangle (size of the list to return).

    Returns:
        list<list<int>>: A list of lists of the coefficients of expansion of
                         power going from 0 to n - 1
    """
    triangle = []
    for i in range(n):
        triangle.append(get_pascal_triangle_line(i))
    return (triangle)
