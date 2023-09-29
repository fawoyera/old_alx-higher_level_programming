#!/usr/bin/python3
"""Module to determine if an object ia an instance of class or superclass"""


def is_kind_of_class(obj, a_class):
    """Function to determine if obj is an instance of a_class"""
    return isinstance(obj, a_class)
