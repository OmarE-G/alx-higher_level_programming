#!/usr/bin/python3
"""module
"""


class Square:
    """Empty class that defines a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        for i in range(self.__size):
            print('#' * self.__size)
        if self.__size == 0:
            print()
    
        
        
    

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
