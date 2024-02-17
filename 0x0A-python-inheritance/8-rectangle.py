#!/usr/bin/python3
"""
Rectangle geometry module
"""
BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """Rectangle class"""
    def __init__(self, width, height):
        self.integer_validator(width)
        self.integer_validator(height)
        self.__width = width
        self.__height = height
