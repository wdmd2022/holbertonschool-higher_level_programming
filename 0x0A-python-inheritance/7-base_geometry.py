#!/usr/bin/python3
"""this module contains an definition of a class"""


class BaseGeometry:
    """this class is a base geometry class for class"""
    def area(self):
        """this method raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """this method validates an integer"""
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise TypeError("<name> must be greater than 0")
