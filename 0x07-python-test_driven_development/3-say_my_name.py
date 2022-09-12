#!/usr/bin/python3
"""this module contains a function to print a name
"""


def say_my_name(first_name, last_name=""):
    """this function prints a name

    Args:
        first_name (str): the first name
        last_name (str, optional): the last name. Defaults to "".

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
