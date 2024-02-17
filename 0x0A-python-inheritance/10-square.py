#!/usr/bin/python3
"""10-square"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
