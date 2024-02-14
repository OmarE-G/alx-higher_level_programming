#!/usr/bin/python3
"""Class my list"""


class my_list(list):
    """list class with print sorted"""
    def print_sorted(self):
        """method to sort a list"""
        print(sorted(self))
