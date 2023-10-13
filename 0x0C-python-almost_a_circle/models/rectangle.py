#!/usr/bin/python3
"""Module for Rectangle class that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """A subclass"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization method for rectangle attributes"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width attribute"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """gets the x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the x attribute"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """gets the y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the y attribute"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """method to compute the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """method to display rectangle using #"""
        print('\n' * self.__y + ((' ' * self.__x + '#' * 
                self.__width + '\n') * self.__height), end="")

    def __str__(self):
        """custom __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, 
self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """public method to update attributes"""
        attr = ['id', 'width', 'height', 'x', 'y']
        largs = len(args)
        if largs != 0:
            for i in range(largs):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """public method to return dictionary representation of rectangle"""
        return {key: getattr(self, key) for key in ['id', 'width', 'height', 'x', 'y']}
