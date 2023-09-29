#!/usr/bin/python3
"""Module that defines a class with two public instance methods"""


class BaseGeometry:
    """Class to validate an integer value"""
    def __init__(self):
        """Initialization method"""
        pass

    def area(self):
        """Method that does nothing"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates an integer value"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry"""
    def __init__(self, width, height):
        """Ïnitialization method for rectangle attributes width and height"""
        BaseGeometry.__init__(self)
        if Rectangle.integer_validator(self, "width", width) is None:
            self.__width = width
        if Rectangle.integer_validator(self, "height", height) is None:
            self.__height = height
