#!/usr/bin/python3
"""Module to write text to a file"""


def write_file(filename="", text=""):
    """Function that writes text to a file
    Args:
            filename --> the (path)name of the file
            text     --> the text to write to file

    Return:
            the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as TextFile:
        return TextFile.write(text)
