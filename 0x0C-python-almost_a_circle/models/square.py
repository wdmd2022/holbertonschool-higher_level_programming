#!/usr/bin/python3
"""this module contains a Square (shaped, not termperaent) class"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """this defines the Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """this initializes the Square"""
        super().__init__(self, size, size, x, y, id)

    def __str__(self):
        twine = "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                          self.y, self.height)
        return twine
