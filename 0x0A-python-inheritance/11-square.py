#!/usr/bin/python3
"""Module that defines a class Square that inherits from subclass Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a Square"""
    def __init__(self, size):
        """Initialization method"""
        if Square.integer_validator(self, "size", size) is None:
            self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Method to find area of square"""
        return self.__size ** 2

    def __str__(self):
        """"Method to print string formatted output"""
        return "[Square] {}/{}".format(self.__size, self.__size)
