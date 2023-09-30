#!/usr/bin/python3
"""Module that defines a class MyInt which inherits from int"""


class MyInt(int):
    """Rebel Class that inherits from int"""
    def __eq__(self, other):
        """Custom method to check for equality. Inverts the operation"""
        if self < other or self > other:
            return True
        else:
            return False

    def __ne__(self, other):
        """Custom method to check for inequality. Inverts the operation"""
        if self < other or self > other:
            return False
        else:
            return True
