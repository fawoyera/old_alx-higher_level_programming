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

    def area(self):
        """Method to find the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """"Method to print string formatted output"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
