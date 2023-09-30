#!/usr/bin/python3
"""Module to write an Object to a text file using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Function to write object to json file"""
    with open(filename, mode="w", encoding="utf-8") as JSONFile:
        json_file = json.dumps(my_obj)
        JSONFile.write(json_file)
