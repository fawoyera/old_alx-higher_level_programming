#!/usr/bin/python3
"""Module that defines class with private var, public method, g(s)etters"""


class Square:
    """Class that defines a square with optional instance variable & method"""
    def __init__(self, size=0):
        """Method that initializes an instance of class Square"""
        try:
            assert type(size) == int or type(size) == float
        except Exception:
            raise TypeError('size must be a number')
        else:
            try:
                assert size >= 0
            except Exception:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size

    @property
    def size(self):
        """Method that gets the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets the size of square"""
        try:
            assert type(value) == int or type(value) == float
        except Exception:
            raise TypeError('size must be a number')
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

    def __eq__(self, other):
        """Method to compare equality of squares based on the square area"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Method to compare non-equality of squares based on squares areas"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Method to compare inequality squares based on the square area"""
        return self.area() < other.area()

    def __le__(self, other):
        """Method to compare inequality of squares based on the square area"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Method to compare inequality of squares based on the square area"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Method to compare inequality of squares based on the square area"""
        return self.area() >= other.area()
