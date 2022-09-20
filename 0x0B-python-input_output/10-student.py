#!/usr/bin/python3
"""this module contains a class Student"""


class Student:
    """this class represents a Student object"""
    def __init__(self, first_name, last_name, age):
        """initializes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """retrieves a dictionary representation of a Student.
        If attrs is a list of strings, only retrieves attributes
        named in the string. Else, retrieves all attributes."""
        if type(attr) == list:
            for item in attr:
                if type(attr) != str:
                    return self.__dict__
                
        return self.__dict__
