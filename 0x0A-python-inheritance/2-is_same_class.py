#!/usr/bin/python3
"""this module contains a function that checks the class of an object"""


def is_same_class(obj, a_class):
    """checks to see if obj is an instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
