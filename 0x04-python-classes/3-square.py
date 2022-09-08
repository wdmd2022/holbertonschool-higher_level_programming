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

    @property
    def size(self):
        """getter for retrieving size of square

        Returns:
            int: size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter to set value of size of square (length of side)

        Args:
            value (int): length of one side of square (must be >= 0)

        Raises:
            ValueError: if there is a negative integer, which is a wild idea
            TypeError: if value is not an integer at all -- even more wild
        """
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """The area method uses complicated math to compute the area

        Returns:
            int: the size (side length) times itself (dare I say, squared?)
        """
        return self.__size * self.__size
