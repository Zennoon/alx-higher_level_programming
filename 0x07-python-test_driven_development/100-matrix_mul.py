#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 100-matrix_mul.py

Author: Yunus Kedir

This module contains:

Functions:
    matrix_mul - Multiplies two matrices if they are valid
    validare_matrix - Helper function for matrix_mul, validates matrices
    transpose - Helper function formatrix_mul, transposes a matrix

"""


def validate_matrix(matrix, name):
    """Validates that a given matrix is valid.

    For this program, a matrix has to satisfy these conditions to be valid
    1. Has to be a list.
    2. Has to be a list of lists.
    3. Has to be non-empty.
    4. Has to be a list of lists of integers or floats.
    5. Has to be rectangular (all rows must have the same size).

    Args:
        matrix (list): The matrix to validate.
        name (str): The name of the matrix, used on error messages.
    """
    if matrix.__class__ is not list:
        raise TypeError("{} must be a list".format(name))

    if len(matrix) > 0 and matrix[0].__class__ is list:
        row_size = len(matrix[0])

    for row in matrix:
        if row.__class__ is not list:
            raise TypeError(f"{name} must be a list of lists")
        for item in row:
            if item.__class__ not in [int, float]:
               raise TypeError(f"{name} should contain only integers or floats")
        if len(row) != row_size:
            raise TypeError(f"each row of {name} must be of the same size")
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError(f"{name} can't be empty")


def transpose(m):
    """Transposes a given matrix.

    Args:
        m (list): The matrix to transpose.

    Returns:
        list: The transpose of m.
    """
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]


def matrix_mul(m_a, m_b):
    """Computes multiplication of two matrices.

    Two matrices can be multiplied only if the number of rows of
    the first matrix is equal to the number of columns of the second.

    Args:
        m_a (list): The first operand.
        m_b (list): The second operand.

    Returns:
        list: Result of the multiplication of the two matrices if
              they are valid, and they can be multiplied.
    """

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_b = transpose(m_b)
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b)):
            sum_of_mul = 0
            for k in range(len(m_a[i])):
                sum_of_mul += m_a[i][k] * m_b[j][k]
            row.append(sum_of_mul)
        result.append(row)
    return (result)
