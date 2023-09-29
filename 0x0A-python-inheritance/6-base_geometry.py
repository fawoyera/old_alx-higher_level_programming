#!/usr/bin/python3
"""Module that defines a class with a public instance method undefined"""


class BaseGeometry:
    """Class with empty method"""
    def area(self):
        """Method that does nothing"""
        raise Exception("area() is not implemented")
