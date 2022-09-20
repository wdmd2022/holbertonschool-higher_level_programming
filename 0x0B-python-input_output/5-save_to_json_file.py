#!/usr/bin/python3
"""contains a function to write an obj to a text file using a JSON rep"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding='UTF-8') as cool_file:
        cool_file.write(json.dumps(my_obj))
