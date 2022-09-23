#!/usr/bin/python3
"""this module contains the Base class"""

import json


class Base():
    """this class represents the Base class we will use"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this method initializes the object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON string rep of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
