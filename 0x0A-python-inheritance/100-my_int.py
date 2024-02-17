#!/usr/bin/python3
"""MY int module"""


class MyInt(int):
    """new modded int"""
    def __eq__(self, __value):
        return self != __value

    def __ne__(self, __value):
        return self == __value
