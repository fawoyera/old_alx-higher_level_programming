#!/usr/bin/python3
"""
Module that creates a class LockedClass with no class or object attribute
"""


class LockedClass(object):
    """Class that prevents the user from dynamically creating new instance
    attribute, except if the new instance attribute is called first_name
    """
    __slots__ = ['first_name']
