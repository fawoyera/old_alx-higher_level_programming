#!/usr/bin/python3
"""
Module to print name to stdout
Args:   first name
        last name
Return: None
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print full name to stdout
    """
    if not type(first_name) == str:
        raise TypeError("first_name must be a string")
    if not type(last_name) == str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
