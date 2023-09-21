#!/usr/bin/python3
""""
Module to print a square with character #
Arguments: size - the size length of the square
Return: None
"""


def print_square(size):
    """
    Function that prints a square using char '#' given its size
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if (type(size) is float) and (size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
