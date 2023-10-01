#!/usr/bin/python3
""""Test module"""
import unittest


class TestTest1(unittest.TestCase):
    """"Test Case Class"""
    def test_test1(self):
        """First Test method"""
        self.assertTrue(True)
        self.assertEqual(1, 1)

    def test_test2(self):
        """Second Test method"""
        with self.assertRaises(ZeroDivisionError):
            1 / 0
