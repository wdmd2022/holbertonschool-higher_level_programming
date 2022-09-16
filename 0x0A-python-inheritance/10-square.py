#!/usr/bin/python3
"""this module uses BaseGeometry to make a square class"""


class BaseGeometry():
    """Defines a class that will be used later"""
    def area(self):
        """ method that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """this is a class to represent Rectangle objects"""
    def __init__(self, width, height):
        """initializes the Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """makes the string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """this makes a subclass of Rectangle"""
    def __init__(self, size):
        """this initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

