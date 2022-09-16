#!/usr/bin/python3
"""this module uses BaseGeometry to make a rectangle class"""


"""first we will import BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is a class to represent Rectangle objects"""
    def __init__(self, width, height):
        super().integer_validator(width)
        self.__width = width
        super().integer_validator(height)
        self.__height = height
