#!/usr/bin/python3
"""this module contains a Rectangle sub-class of Base"""


class Rectangle(Base):
    """this class represents a Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """here we initialize the Rectangle"""
        if id is not None:
            self.id = id
        else:
            super().__nb_objects += 1
            self.id = super().__nb_objects
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for retrieving width of rectangle

        Returns:
            int: size of the square
        """

        return self.__width

    def width(self, value):
        """setter to set value of width of rectangle

        Args:
            value (int): width of the rectangle

        Raises:
            ValueError: if there is a 0 or negative int, which is a wild idea
            TypeError: if value is not an integer at all -- even more wild
        """
        if type(value) == int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter for retrieving height of rectangle

        Returns:
            int: height of the rectangle
        """

        return self.__height

    def height(self, value):
        """setter to set value of height of rectangle

        Args:
            value (int): height of the rectangle

        Raises:
            ValueError: if there is a 0 or negative int, which is a wild idea
            TypeError: if value is not an integer at all -- even more wild
        """
        if type(value) == int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """getter for retrieving x value of rectangle

        Returns:
            int: x
        """

        return self.__x

    def x(self, value):
        """setter to set x value of rectangle

        Args:
            value (int): x value of the rectangle

        Raises:
            ValueError: if there is a negative integer, which is a wild idea
            TypeError: if value is not an integer at all -- even more wild
        """
        if type(value) == int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """getter for retrieving y value of rectangle

        Returns:
            int: y
        """

        return self.__y

    def y(self, value):
        """setter to set y value of rectangle

        Args:
            value (int): y value of the rectangle

        Raises:
            ValueError: if there is a negative integer, which is a wild idea
            TypeError: if value is not an integer at all -- even more wild
        """
        if type(value) == int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
