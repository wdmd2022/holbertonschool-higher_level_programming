#!/usr/bin/python3
"""This module contains a class to make a square object"""

class Square:
    """This class defines an empty, square-like object"""
    
    def __init__(self, size=0):
        """The __init___ method creates a square

        Args:
            size (int, optional): length of a side. Defaults to 0.
        """
        self.__size = size
