#!/usr/bin/python3
"""Module to define a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Ïnitialization method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Custom __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, 
self.x, self.y, self.width)

    @property
    def size(self):
        """getter method for size of square"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method for size of square"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.height = self.width = size

    def update(self, *args, **kwargs):
        """method to update attributes of square"""
        attr = ['id', 'size', 'x', 'y']
        largs = len(args)
        if largs != 0:
            for i in range(largs):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """public method to return dictionary representation of a square"""
        return {key: getattr(self, key) for key in ['id', 'size', 'x', 'y']}
