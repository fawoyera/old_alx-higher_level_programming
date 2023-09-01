#!/usr/bin/python3
"""Module that defines class with private var, public method, g(s)etters"""


class Square:
    """Class that defines a square with optional instance variable & method"""
    def __init__(self, size=0):
        """Method that initializes an instance of class Square"""
        self.__size = size

    @property
    def size(self):
        """Method that gets the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets the size of square"""
        try:
            assert type(value) == int
        except Exception:
            raise TypeError('size must be an integer')
        else:
            try:
                assert value >= 0
            except Exception:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        """Method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Method that prints a square using #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("{:s}".format('#' * self.__size))
