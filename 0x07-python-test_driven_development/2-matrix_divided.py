#!/usr/bin/python3
"""Module to divide all elements of a matrix
    Args:   matrix  - the matrix to divide
            div     - the divisor
    Return: the new matrix
"""


def matrix_divided(matrix, div):
    """
    Method to divide a matrix
    """
    if not type(matrix) == list:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for row in matrix:
        if not type(row) == list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        for element in row:
            if not type(element) in [int, float]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(list(float("{:.2f}".format(element / div))
                     for element in row) for row in matrix)
