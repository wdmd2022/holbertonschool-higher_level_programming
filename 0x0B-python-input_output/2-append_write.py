#!/usr/bin/python3
"""This module contains a function that appends text to a file"""


def append_write(filename="", text=""):
    """this function appends a string to a file"""
    with open(filename, mode="a", encoding='UTF-8') as mr_file:
        charswritten = mr_file.write(text)
        return charswritten
