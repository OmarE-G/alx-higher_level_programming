#!/usr/bin/python3
"""Class my list"""


class my_list(list):
    """list class with print sorted"""
    def print_sorted(self):
        print(sorted(self))
