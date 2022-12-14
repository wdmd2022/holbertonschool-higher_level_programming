#!/usr/bin/python3
"""this module contains a new class that inherits from list"""


class MyList(list):
    """a class that inherits from the list class"""
    def __init__(self):
        """initializes the MyList object"""
        super().__init__()

    def print_sorted(self):
        """prints it in a sorted, ascending manner"""
        print(sorted(self))
