#!/usr/bin/python3
"""this module contains a Rectangle sub-class of Base"""

from models.base import Base


class Rectangle(Base):
    """this class represents a Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """here we initialize the Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for retrieving width of rectangle

        Returns:
            int: size of the square
        """

        return self.__width

    @width.setter
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

    @height.setter
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

    @x.setter
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

    @y.setter
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

    def area(self):
        """method that returns the area"""
        return self.__height * self.__width

    def display(self):
        """method that draws a pretty rectangle"""
        for number in range(self.__y):
            print("")
        for row in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            print("#" * self.__width)

    def __str__(self):
        """makes a cool string representation"""
        stringywingy = "[Rectangle] (" + str(self.id) + ") " + str(self.__x) \
                       + "/" + str(self.y) + " - " + str(self.__width) + "/" \
                       + str(self.__height)
        return stringywingy

    def update(self, *args, **kwargs):
        """updates values of the rectangle"""
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)
