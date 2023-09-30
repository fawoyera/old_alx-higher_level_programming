#!/usr/bin/python3
"""Module to serialize a python object string"""

import json


def to_json_string(my_obj):
    """Function to serialize an object to json string"""
    return json.dumps(my_obj)
