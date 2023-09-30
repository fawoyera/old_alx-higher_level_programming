#!/usr/bin/python3
"""Module that prints the dictionary description of simple data structures"""


def class_to_json(obj):
    """Function to serialize the dictionary of obj"""
    return obj.__dict__
