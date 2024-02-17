#!/usr/bin/python3
"""
===========
Square geometry module
===========
"""
R = __import__('9-Rectangle').Rectangle


class Square(R):
    """Square class"""
    def __init__(self, size):
        """initialize square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of square"""
        return R.area(self.__size, self.__size)
