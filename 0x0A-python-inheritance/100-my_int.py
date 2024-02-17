#!/usr/bin/python3
"""MY int module"""


class MyInt(int):
    """new modded int"""
    def __eq__(self, value) -> bool:
        return super().__ne__(value)

    def __ne__(self, value) -> bool:
        return super().__eq__(value)
