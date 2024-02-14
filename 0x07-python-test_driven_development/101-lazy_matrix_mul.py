#!/usr/bin/python3
# -*- coding: utf-8
""" 101-lazy_matrix_mul

This module contains:

Functions:
    lazy_matrix_mul - Multiplies two matrices using numpy and returns result as
                      list

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using the numpy library.

    Args:
        m_a (list): First operand.
        m_b (list): Second operand.

    Returns:
        list: Result of the multiplication of m_a, and m_b.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    return ([list(arr) for arr in np.matmul(m_a, m_b)])
