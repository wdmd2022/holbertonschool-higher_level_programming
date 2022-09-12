#!/usr/bin/python3
"""this module contains a function to print a square
"""


def print_square(size):
    """this function prints a square w/ side length size

    Args:
        size (int): length of the side

    Raises:
        TypeError: if size is not an int
        ValueError: if size is < 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
