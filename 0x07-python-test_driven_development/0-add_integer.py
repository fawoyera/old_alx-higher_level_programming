#!/usr/bin/python3
"""Module to add 2 integers
    Args: a: first integer
          b: second integer
    Return: sum of integers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
