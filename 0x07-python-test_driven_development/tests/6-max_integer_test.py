#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class to test the method 'max_integer'
    """
    def test_max_integer(self):
        """
        Test case method for 'max_integer'
        """
        self.assertEqual(max_integer([3, 5, 1, 2]), 5)
        self.assertEqual(max_integer([7, 3, 9, 34, 5, 90, 67]), 90)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_type(self):
        """Test case method to check if Exception is raised 
           when input is not a list of integers
        """
        self.assertRaises(TypeError, max_integer, ['a', 5, "sit"])
        self.assertRaises(TypeError, max_integer, 4)
