#!/usr/bin/python3
"""This module contains a class to make a square object"""


class Square:

    """This class defines a square-like object"""

    def __init__(self, size=0):
        """The __init___ method creates a square

        Args:
            size (int, optional): length of a side. Defaults to 0.
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
