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
    i = 0
    while i < len(text):
        """
        if (text[char - 1] in ['.', '?', ':']) and (text[char] == " "):
            continue
        """
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print('\n')
            if (i + 1) < len(text):
                while text[i + 1] == " ":
                    i = i + 1
        i = i + 1
