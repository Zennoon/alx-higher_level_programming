#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-matrix_divided.py

Author: Yunus Kedir

This module is the second one in the series for Test Driven Development. It
has doctest unit tests in the tests directory found in the current folder.

"""


def matrix_divided(matrix, div):
    """Divides each element of a given matrix by a given divider and returns
    a new matrix holding the resulting numbers (rounded to 2 decimal places).

    The function performs argument validation for both the arguments.
    1. matrix has to be a list of lists of integers or floats.
    2. Each row of the matrix must have the same size.
    3. div must be an integer or a float.
    4. div cannot be 0.

    Args:
        matrix (list<list<int>>): The matrix whose elements are divided.
        div (int/float): The number which the elements of the matrix are divided
        by.

    Returns:
        list<list<int>>: A list of lists holding the results of the division of
        the corresponding elements of matrix by div.

    """
    if matrix.__class__ is not list:
        raise TypeError("matrix must be a matrix (list of lists) of " +
                        "integers/floats")
    if div.__class__ not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    if matrix[0].__class__ is list:
        row_len = len(matrix[0])
    for row in matrix:
        if row.__class__ is not list:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if elem.__class__ not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of " +
                                "integers/floats")
            new_row.append(round(elem / div, 2))
        new_matrix.append(new_row)
    return (new_matrix)
