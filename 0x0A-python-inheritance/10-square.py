#!/usr/bin/python3
"""Module that defines a class Square that inherits from subclass Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square"""
    def __init__(self, size):
        """Initialization method"""
        Rectangle.__init__(self, size, size)
        if Square.integer_validator(self, "size", size) is None:
            self.__size = size

    def area(self):
        """Method to find area of square"""
        return self.__size ** 2
