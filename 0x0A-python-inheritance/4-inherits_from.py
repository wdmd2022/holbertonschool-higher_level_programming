#!/usr/bin/python3
"""this module contains the function inherits_from"""


def inherits_from(obj, a_class):
    """returns true if obj inherits from a_class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
