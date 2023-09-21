#!/usr/bin/python3
"""
Module to indent text by print 2 new lines after ., ? and :
Args: text - the tezt string to indent
Return: None
"""


def text_indentation(text):
    """
    Function to indent text by printing 2 new lines after ., ? and :
    """
    if not type(text) is str:
        raise TypeError("text must be a string")
    for char in range(len(text)):
        """
        if (text[char - 1] in ['.', '?', ':']) and (text[char] == " "):
            continue
        """
        print(text[char], end="")
        if text[char] in ['.', '?', ':']:
            print('\n')
