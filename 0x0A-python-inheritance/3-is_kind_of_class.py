#!/usr/bin/python3
"""this module contains the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns true if obj is an instance of class a_class or a
    type that inherits from a_class
    """
    if type(obj) == a_class or issubclass(obj, a_class):
        return True
    else:
        return False
