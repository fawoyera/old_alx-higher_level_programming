#!/usr/bin/python3
"""Module that creates a function that add new attributes to an object"""


def add_attribute(obj, new_attr, value):
    """Function that add new attributes to the object obj
    Args:
            obj     --> the object
            new_attr--> the new attribute to add (string)
            value   --> the value of the attribute to set

    Return:
            None
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, new_attr, value)
