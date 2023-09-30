#!/usr/bin/python3
"""Module that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Function that appends a string to the end of a text file
    Args:
            filename --> the (path)name of the text file
            text     --> the text to append to file end

    Return:
            the number of characters appended to file end
    """
    with open(filename, mode="a", encoding="utf-8") as TextFile:
        return TextFile.write(text)
