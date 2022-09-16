#!/usr/bin/python3
"""this module contains a function that checks the class of an object"""


def is_same_class(obj, a_class):
    """checks to see if obj is exactly an instance of class"""
    return (type(obj) == a_class)
