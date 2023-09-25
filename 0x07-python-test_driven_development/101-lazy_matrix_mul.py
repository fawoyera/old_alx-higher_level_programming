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
    if (type(m_a) is str) or (type(m_b) is str):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    for item in m_a:
        for items in item:
            if type(items) is str:
                raise TypeError("invalid data type for einsum")
    for item in m_b:
        for items in item:
            if type(items) is str:
                raise TypeError("invalid data type for einsum")

    """ïnitialize result matrix with zeros"""
    result = [[0 for j in range(len(m_b[0]))] for i in range(len(m_a))]

    result = np.dot(m_a, m_b)

    return result
