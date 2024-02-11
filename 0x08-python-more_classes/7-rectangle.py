#!/usr/bin/python3
"""module
"""


class Rectangle:
    """rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __str__(self):
        str = ""
        for i in range(self.height):
            str += Rectangle.print_symbol * self.width
            if i != self.height - 1:
                str += '\n'
        if self.area() == 0:
            str = ""
        return str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.area() > 0) * (self.width * 2 + self.height * 2)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, val):
        if not type(val) is int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @height.setter
    def height(self, val):
        if not type(val) is int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val
