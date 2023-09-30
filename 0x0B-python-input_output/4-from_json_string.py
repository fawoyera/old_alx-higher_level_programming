#!/usr/bin/python3
"""Module that deserialize a json string to python object string"""


import json


def from_json_string(my_str):
    """Function that deserializes a json string"""
    return json.loads(my_str)
