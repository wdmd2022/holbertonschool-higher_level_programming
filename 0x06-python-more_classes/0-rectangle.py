#!/usr/bin/python3
"""this module contains a class definition for Rectangle object

    Raises:
        ValueError: if instaniated width is < 0
        TypeError: if instantiated width is non-int
        ValueError: if instantiated height is < 0
        TypeError: if instantiated height is non-int
        ValueError: if width setter receives value < 0
        TypeError: if width setter receives non-int value
        ValueError: if height setter receives value < 0
        TypeError: if height setter receives non-int value

    Returns:
        int: when getting height or width
    """


class Rectangle:
    """this class defines Rectangles
    """

    def __init__(self, width=0, height=0):
        """this function instantiates an object of Rectangle class

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.

        Raises:
            ValueError: if width < 0
            TypeError: if width is non-integer
            ValueError: if height is < 0
            TypeError: if height is non-integer
        """
        if type(width) == int:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        if type(height) == int:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """getter for width of rectangle

        Returns:
            int: private width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width of rectangle

        Args:
            value (int): width of rectangle to set

        Raises:
            ValueError: if width is not >= 0
            TypeError: if width is not an int
        """
        if type(value) == int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter for height of rectangle

        Returns:
            int: private height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height of rectangle

        Args:
            value (int): height of rectangle to set

        Raises:
            ValueError: if height is not >= 0
            TypeError: if height is not an int
        """
        if type(value) == int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
