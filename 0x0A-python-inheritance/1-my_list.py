#!/usr/bin/python3
"""Module that sorts a list in ascending order and prints it"""


class MyList(list):
    """Class that defines the methods to sort the list"""
    def print_sorted(self):
        """"Method to sort the list in ascending order"""
        new_list = super().copy()
        new_list.sort()
        print(new_list)
