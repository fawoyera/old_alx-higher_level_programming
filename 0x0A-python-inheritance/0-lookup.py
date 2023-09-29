#!/usr/bin/python3
"""Module to return the list of available attributes & methods of an object"""


def lookup(obj):
    """Function to return list of the attributes and methods of object"""
    return dir(obj)
