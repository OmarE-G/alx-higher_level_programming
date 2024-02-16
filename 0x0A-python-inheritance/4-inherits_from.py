#!/usr/bin/python3


"""
def is_kind_of_class(obj, a_class): module
"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class; otherwise False."""
    return issubclass(obj, a_class)
