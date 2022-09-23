#!/usr/bin/python3
"""this module contains a Square (shaped, not termperaent) class"""

from models.rectangle import Rectangle
from models.base import Base


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

    def update(self, *args, **kwargs):
        """updates values of the square"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)

    def to_dictionary(self):
        """this method returns a dictionary representation"""
        llcooldict = {}
        llcooldict['id'] = self.id
        llcooldict['x'] = self.x
        llcooldict['size'] = self.size
        llcooldict['y'] = self.y
        return llcooldict
