#!/usr/bin/python3
"""module
"""


class Square:
    """Empty class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        str = '\n' * self.position[1] * int(self.size != 0)
        for i in range(self.size):
            str += self.position[0] * ' ' + '#' * self.size
            if i != self.size - 1:
                str += '\n'
        return str

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            print('\n' * self.position[1], end='')
            for i in range(self.__size):
                print(' ' * self.position[0] + '#' * self.__size)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    @position.setter
    def position(self, value):
        if not (type(value) is tuple
                and len(value) == 2
                and all((type(i) is int and i >= 0) for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
