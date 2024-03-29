#!/usr/bin/python3


"""
Base geometry module
"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """area function"""
        raise Exception("area() is not implemented")

    
    def integer_validator(self, name, value):
        """validate int value"""
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
