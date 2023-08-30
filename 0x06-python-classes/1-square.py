#!/usr/bin/python3
"""Module that defines a square with a private instance attribute"""


class Square:
    """class that defines a private instance attribute"""
    def __init__(self, size):
        """initialization function for square instance"""
        self.__size = size
