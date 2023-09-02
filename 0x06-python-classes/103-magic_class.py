#!/usr/bin/python3
"""Module that does exactly the same as given python bytecode"""
import math


class MagicClass:
    """Class that does same as byte code"""
    def __init__(self, radius):
        """Method that initializes an instance of the class MagicClass"""
        try:
            assert type(radius) is not int or type(radius) is not float
        except Exception:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Method to compute area of circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Method to compute circumference of circle"""
        return 2 * math.pi * self.__radius ** 2
