#!/usr/bin/python3
"""Module that defines a class Rectangle with public methods area and perimeter
    with __str__ and __repr__ methods
"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialization method
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter method for width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width of rectangle
        """
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method for height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height of rectangle
        """
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        method to find the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        method to find the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        str method to print rectangle using #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += "{}".format(self.print_symbol) * self.__width + '\n'
        string = string[:-1]
        return string

    def __repr__(self):
        """
        repr method to print class instance (object)
        """
        return "Rectangle(" + str(self.__width) + ","\
                            + str(self.__height) + ")"

    def __del__(self):
        """
        del method to print message when class instance is being deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
