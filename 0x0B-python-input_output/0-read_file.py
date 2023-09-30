#!/usr/bin/python3
"""Module that defines a function that raeds froma textfile"""


def read_file(filename=""):
    """"Function that reads from a textfile
    Args:
            filename --> the (path)name of the textfile

    Return:
            None
    """
    with open(filename, mode="r", encoding="utf-8") as TextFile:
        print(TextFile.read(), end="")
