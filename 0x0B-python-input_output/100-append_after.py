#!/usr/bin/python3
"""Module that append new line of string after lines containing given text"""


def append_after(filename="", search_string="", new_string=""):
    """Function that apppends a new line to file after lines with text"""
    new_file = ""
    with open(filename, mode="r", encoding="utf-8") as fp:
        for line_read in fp:
            new_file += line_read
            if search_string in line_read:
                new_file += new_string

    with open(filename, mode="w", encoding="utf-8") as fp2:
        fp2.write(new_file)
