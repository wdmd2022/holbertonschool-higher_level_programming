#!/usr/bin/python3
"""This module contains a function that reads/prints a file to stdout"""


def read_file(filename=""):
    with open(filename, mode="r", encoding='UTF-8') as mr_file:
        for line in mr_file:
                print("{}".format(line), end="")
