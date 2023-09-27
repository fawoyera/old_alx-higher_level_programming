#!/usr/bin/python3
"""
Module that creates a class LockedClass with no class or object attribute
"""


class LockedClass(object):
    """Class that prevents the user from dynamically creating new instance
    attribute, except if the new instance attribute is called first_name
    """
    def __init__(self):
        """
        initialization method for class instance
        """
        pass

    def __setattr__(self, key, value):
        """
        method to set instance attribute if it is firstname
        """
        if key != "first_name":
            raise AttributeError("'{}' object has no attribute \
'{}'".format(self.__class__.__name__, key))
        object.__setattr__(self, key, value)
