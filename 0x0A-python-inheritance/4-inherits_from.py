#!/usr/bin/python3
"""Module to check if an object is an instance of a class which inherits"""


def inherits_from(obj, a_class):
    """"Function to check if object is instance of sub_class"""
    if type(obj).__name__ == a_class.__name__:
        return False
    return isinstance(obj, a_class)
