#!/usr/bin/python3
"""MY int module"""


class MyInt(int):
    """new modded int"""

    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return other != self.value

    def __ne__(self, other):
        return other == self.__value
