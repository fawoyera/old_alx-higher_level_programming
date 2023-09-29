#!/usr/bin/python3
"""Module that defines a class with two public instance methods"""


class BaseGeometry:
    """Class with empty method"""
    def area(self):
        """Method that does nothing"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates an integer value"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
