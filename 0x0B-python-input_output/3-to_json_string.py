#!/usr/bin/python3
"""contains a function that returns an obj's JSON representation"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
