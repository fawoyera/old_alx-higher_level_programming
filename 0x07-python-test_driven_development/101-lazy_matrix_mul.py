#!/usr/bin/python3
"""
Module to multiply two matrice using the NumPy module
Args:   m_a --> the first matrix
        m_b --> the second matrix
Return: the product of the two matrices if possible
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Module to multiply two matrices (m_a) and (m_b)
    """
    if not type(m_a) is list:
        raise TypeError("m_a must be a list")
    if not type(m_b) is list:
        raise TypeError("m_b must be a list")
    for item in m_a:
        if not type(item) is list:
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if not type(item) is list:
            raise TypeError("m_b must be a list of lists")
    if (len(m_a) == 0) or (len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if (len(m_b) == 0) or (len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    for item in m_a:
        for items in item:
            if not type(items) in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for item in m_b:
        for items in item:
            if not type(items) in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    length_0 = len(m_a[0])
    for item in m_a:
        if len(item) != length_0:
            raise TypeError("each row of m_a must be of the same size")
    length_1 = len(m_b[0])
    for item in m_b:
        if len(item) != length_1:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """ïnitialize result matrix with zeros"""
    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    result = np.dot(m_a, m_b)

    return result
