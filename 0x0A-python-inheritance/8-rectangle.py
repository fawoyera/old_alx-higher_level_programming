#!/usr/bin/python3
"""Module that defines a class with two public instance methods"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry"""
    def __init__(self, width, height):
        """Ïnitialization method for rectangle attributes width and height"""
        if Rectangle.integer_validator(self, "width", width) is None:
            self.__width = width
        if Rectangle.integer_validator(self, "height", height) is None:
            self.__height = height
