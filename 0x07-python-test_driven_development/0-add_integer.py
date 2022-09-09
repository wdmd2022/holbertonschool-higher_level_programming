#!/usr/bin/python3
"""This module contains a function to add integers
"""


def add_integer(a, b=98):
    """This function adds two integers

    Args:
        a (int): the first integer to add
        b (int, optional): The second integer. Defaults to 98.

    Raises:
        TypeError: if user doesn't enter an integer for a
        TypeError: if user enters a non-integer b

    Returns:
        int: the sum of addition
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
