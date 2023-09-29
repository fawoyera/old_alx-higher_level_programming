#!/usr/bin/python3
"""Module to determine if an object is exactly an instance of given class"""


def is_same_class(obj, a_class):
    """Function to determine if object belong to a given class"""
    return type(obj).__name__ == a_class.__name__
