#!/usr/bin/python3
"""this module contains a Square (shaped, not termperaent) class"""

from ctypes import sizeof
from models.rectangle import Rectangle


class Square(Rectangle):
    """this defines the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """this initializes the Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        twine = "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                          self.y, self.height)
        return twine

    @property
    def size(self):
        """getter for retrieving size of square object"""
        return self.height

    @size.setter
    def size(self, value):
        """sets size of square"""
        self.width = value
        self.height = value
