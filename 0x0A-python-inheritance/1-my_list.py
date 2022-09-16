#!/usr/bin/python3
"""this module contains a new class that inherits from list"""


class MyList(list):
    def __init__(self):
        """initializes the MyList object"""
        super().__init__(self)

    def print_sorted(self):
        """prints it in a sorted, ascending manner"""
        print(sorted(self))
