#!/usr/bin/python3
"""this module has a function that uses a JSON file to create an object"""

import json


def load_from_json_file(filename):
    """this function creates an object from a JSON file"""
    with open(filename, "r", encoding="UTF-8") as ll_cool_file:
        return json.load(ll_cool_file)
