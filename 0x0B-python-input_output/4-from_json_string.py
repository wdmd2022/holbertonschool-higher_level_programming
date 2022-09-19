#!/usr/bin/python3
"""contains a function to return an obj from a JSON str"""
import json


def from_json_string(my_str):
    """returns a Python obj represented by a JSON string"""
    return json.loads(my_str)
