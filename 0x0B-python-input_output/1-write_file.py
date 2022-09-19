#!/usr/bin/python3
"""This module contains a function that (over)writes to a file"""


def write_file(filename="", text=""):
    """this function (over)writes to a file"""
    with open(filename, mode="w", encoding='UTF-8') as mr_file:
        charswritten = mr_file.write(text)
        return charswritten
