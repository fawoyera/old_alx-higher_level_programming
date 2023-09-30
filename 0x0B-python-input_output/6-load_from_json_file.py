#!/usr/bin/python3
"""Module to create an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """Function to create an Object from a JSON file"""
    with open(filename, mode="rb") as JSONFile:
        JSONObject = JSONFile.read()
        return json.loads(JSONObject)
