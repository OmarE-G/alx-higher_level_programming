#!/usr/bin/python3
"""MY int module"""


class MyInt(int):
    """new modded int"""
    def __eq__(self, __value: object) -> bool:
        return super().__neq__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
