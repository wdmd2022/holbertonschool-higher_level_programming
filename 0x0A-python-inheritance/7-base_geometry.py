#!/usr/bin/python3
""" this module contains BaseGeometry """


class BaseGeometry():
    """ Defines a class that will be used later """
    def area(self):
        """ method that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
