#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """function to lookup attributes"""
    return list(obj.__dict__)
