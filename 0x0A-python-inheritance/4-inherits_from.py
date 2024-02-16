#!/usr/bin/python3


"""
def inherits_from(obj, a_class):
"""


def inherits_from(obj, a_class):
    """ returns True if the object inherited from class"""
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
