#!/usr/bin/python3
"""Test module for a class Square"""
import unittest
from models.square import Square, Rectangle, Base


class TestSquare(unittest.TestCase):
    """Test class for Square"""
    def test_class(self):
        """test if Square is a subclass of Rectangle and Base"""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test___init__(self):
        """test initialization of the square"""
        with self.assertRaises(TypeError):
            Rec = Square()
        Rec1 = Square(4)
        self.assertEqual(Rec1.width, 4)
        self.assertEqual(Rec1.height, 4)
        self.assertEqual(Rec1.x, 0)
        self.assertEqual(Rec1.y, 0)
        Rec2 = Square(7, 3, 4, 9)
        self.assertEqual(Rec2.width, 7)
        self.assertEqual(Rec2.height, 7)
        self.assertEqual(Rec2.x, 3)
        self.assertEqual(Rec2.y, 4)
        self.assertEqual(Rec2.id, 9)
        Rec3 = Square(9, 8)
        self.assertEqual(Rec3.width, 9)
        self.assertEqual(Rec3.height, 9)
        self.assertEqual(Rec3.x, 8)
        self.assertEqual(Rec3.y, 0)
        Rec4 = Square(4, 1, 8)
        self.assertEqual(Rec4.width, 4)
        self.assertEqual(Rec4.height, 4)
        self.assertEqual(Rec4.x, 1)
        self.assertEqual(Rec4.y, 8)

    def test___str__(self):
        """test custom __str__ method"""
        self.assertEqual(print(Square(3, 4, 3, 3)), None)
        self.assertEqual(print(Square(4, 9)), None)

    def test_getter(self):
        """test the getter method for size of square"""
        self.assertEqual(Square(3, 5).size, 3)
        self.assertEqual(Square(1, 2, 3, 4).size, 1)

    def test_setter(self):
        """test the setter mathod for size of square"""
        Rec = Square(4)
        Rec.size = 14
        self.assertEqual(Rec.size, 14)
        Rec1 = Square(3, 5)
        Rec1.size = 7
        self.assertEqual(Rec1.size, 7)
        Rec2 = Square(2, 4, 6)
        Rec2.size = 11
        self.assertEqual(Rec2.size, 11)
        Rec3 = Square(3, 4, 8, 3)
        Rec3.size = 12
        self.assertEqual(Rec3.size, 12)

    def test_update(self):
        """test the update method for attributes of square"""
        Rec1 = Square(4)
        Rec1.update(7)
        self.assertEqual(Rec1.id, 7)
        Rec2 = Square(3, 5, 7, 9)
        self.assertEqual(Rec2.id, 9)
        self.assertEqual(Rec2.width, 3)
        self.assertEqual(Rec2.height, 3)
        self.assertEqual(Rec2.x, 5)
        self.assertEqual(Rec2.y, 7)
        Rec2.update(1, 2, 3, 4)
        self.assertEqual(Rec2.id, 1)
        self.assertEqual(Rec2.width, 2)
        self.assertEqual(Rec2.height, 2)
        self.assertEqual(Rec2.x, 3)
        self.assertEqual(Rec2.y, 4)
        Rec2.update(2, 4, 5, id=9)
        self.assertEqual(Rec2.id, 2)
        self.assertEqual(Rec2.width, 4)
        self.assertEqual(Rec2.height, 4)
        self.assertEqual(Rec2.x, 5)
        self.assertEqual(Rec2.y, 4)
        Rec2.update(x=9, id=3, size=7, y=11)
        self.assertEqual(Rec2.id, 3)
        self.assertEqual(Rec2.width, 7)
        self.assertEqual(Rec2.height, 7)
        self.assertEqual(Rec2.x, 9)
        self.assertEqual(Rec2.y, 11)
        Rec2.update(y=34, size=23)
        self.assertEqual(Rec2.id, 3)
        self.assertEqual(Rec2.width, 23)
        self.assertEqual(Rec2.height, 23)
        self.assertEqual(Rec2.x, 9)
        self.assertEqual(Rec2.y, 34)

    def test_to_dictionary(self):
        """test the public method to_dictionary of square"""
        Sq = Square(4, 6, 9, 2)
        self.assertEqual(Sq.to_dictionary(), {'size': 4, 'x': 6, 'y': 9, 'id': 2})
        Sq.update(12, 45, 2, 9)
        self.assertEqual(Sq.to_dictionary(), {'id': 12, 'size': 45, 'x': 2, 'y': 9})
