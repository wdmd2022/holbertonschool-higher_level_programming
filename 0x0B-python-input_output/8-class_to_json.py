#!/usr/bin/python3
"""this module contains a function class_to_json"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization
    of an object, with simple data structure (list, dictionary,
    string, integer and boolean"""
    return obj.__dict__
