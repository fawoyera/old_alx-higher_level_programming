#!/usr/bin/python3
"""Module that defines a class with optional instance variable size"""


class Square:
    """Class that defines a square with optional instance variable size"""
    def __init__(self, size=0):
        """Function that initializes an instance of class Square"""
        try:
            assert type(size) == int
        except Exception:
            raise TypeError('size must be an integer')
        else:
            try:
                assert size >= 0
            except Exception:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
