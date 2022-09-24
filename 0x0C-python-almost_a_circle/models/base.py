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

    @classmethod
    def save_to_file(cls, list_objs):
        """this method writes the JSON string rep of list_objs to a file"""
        llcoollist = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for item in list_objs:
                llcoollist.append(cls.to_dictionary(item))
        with open(filename, 'w', encoding="UTF-8") as thefile:
            thefile.write(cls.to_json_string(llcoollist))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            emptylist = []
            return emptylist
        awesomelist = json.loads(json_string)
        return awesomelist

    @classmethod
    def create(cls, **dictionary):
        """creates a dummy object and updates using dictionary"""
        if cls.__name__ == "Square":
            dumbo = cls(123)
        if cls.__name__ == "Rectangle":
            dumbo = cls(123, 456)
        dumbo.update(**dictionary)
        return dumbo

    @classmethod
    def load_from_file(cls):
        """"returns a list of instances"""
        filename = cls.__name__ + ".json"
        ll_cool_list = []
        try:
            with open(filename, "r", encoding="UTF-8") as da_file:
                ll_cool_list = cls.from_json_string(da_file.read())
        except:
            return ll_cool_list
        return ll_cool_list
