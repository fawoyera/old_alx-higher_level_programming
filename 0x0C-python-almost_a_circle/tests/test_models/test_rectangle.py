#!/usr/bin/python3
"""Test module for class Rectangle"""
import unittest, sys
sys.path.insert(0, './models/')
from rectangle import Rectangle, Base


class TestRectangle(unittest.TestCase):
    """Test case for Rectangle class"""
    def test_rectangle(self):
        """test the rectangle subclass"""
        self.assertTrue(issubclass(Rectangle, Base), 'Not a subclass')

    def test_init(self):
        """test proper class instantiation with 2 required arguments"""
        with self.assertRaises(TypeError):
            p = Rectangle()
            p = Rectangle(3)
        self.assertEqual(Rectangle(2, 3).width, 2)
        self.assertEqual(Rectangle(2, 3).height, 3)
        self.assertEqual(Rectangle(2, 3, 5, 7).x, 5)
        self.assertEqual(Rectangle(2, 3, 5, 7).y, 7)
        self.assertEqual(Rectangle(2, 3, 5, 7, 9).id, 9)
        self.assertEqual(Rectangle(2, 3).x, 0)
        self.assertEqual(Rectangle(2, 3).y, 0)
        Rec1 = Rectangle(2, 7)
        self.assertTrue(isinstance(Rec1, Rectangle))
        self.assertTrue(isinstance(Rec1, Base))

    def test_width(self):
        """test the width instance private attribute"""
        with self.assertRaises(AttributeError):
            m = Rectangle(4, 5).width
            n = Rectangle(2, 3).__width
            n = Rectangle.width
            o = Rectangle.__width
            Rectangle(7, 3).width = 7
            Rectangle(4, 5).__width = 4
        self.assertEqual(Rectangle(7, 3).width, 7)
        Rec2 = Rectangle(7, 5)
        self.assertEqual(Rec2.width, 7)
        Rec2.width = 9
        self.assertEqual(Rec2.width, 9)

    def test_height(self):
        """test the height instance private attribute"""
        pass
        with self.assertRaises(AttributeError):
            m = Rectangle(4, 5).height
            n = Rectangle(2, 3).__height
            n = Rectangle.height
            o = Rectangle.__height
            Rectangle(7, 3).height = 3
            Rectangle(4, 5).__height = 5
        self.assertEqual(Rectangle(7, 3).height, 3)
        Rec2 = Rectangle(7, 5)
        self.assertEqual(Rec2.height, 5)
        Rec2.height = 11
        self.assertEqual(Rec2.height, 11)

    def test_x(self):
        """test the x instance private attribute"""
        pass
        with self.assertRaises(AttributeError):
            m = Rectangle(4, 5).x
            n = Rectangle(2, 3).__x
            n = Rectangle.x
            o = Rectangle.__x
            Rectangle(7, 3, 1, 2).x = 1
            Rectangle(4, 5, 2, 3).__x = 2
        self.assertEqual(Rectangle(7, 3, 1, 3).x, 1)
        Rec2 = Rectangle(7, 5, 3, 5)
        self.assertEqual(Rec2.x, 3)
        Rec2.x = 8
        self.assertEqual(Rec2.x, 8)

    def test_y(self):
        """test the y instance private attribute"""
        pass
        with self.assertRaises(AttributeError):
            m = Rectangle(4, 5).y
            n = Rectangle(2, 3).__y
            n = Rectangle.y
            o = Rectangle.__y
            Rectangle(7, 3, 2, 5).y = 7
            Rectangle(4, 5, 1, 1).__y = 4
        self.assertEqual(Rectangle(7, 3, 2, 7).y, 7)
        Rec2 = Rectangle(7, 5, 1, 4)
        self.assertEqual(Rec2.y, 4)
        Rec2.y = 20
        self.assertEqual(Rec2.y, 20)

    def test_id(self):
        """test the id instance attribute"""
        self.assertEqual(Rectangle(2, 5, 7, 3, 5).id, 5)
        Rec3 = Rectangle(2, 5, 7, 3, 12)
        Rec3.id = 6
        self.assertEqual(Rec3.id, 6)

    def test_attr_type(self):
        """test for non-integer attributes"""
        with self.assertRaises(TypeError):
            rec1 = Rectangle("me", 4)
            rec2 = Rectangle(5, {"me": 5})
            rec3 = Rectangle(2, 4, [1], 8)
            rec4 = Rectangle(3, 5, 2, (2, 3))

    def test_attr_value(self):
        """test for non-positive attributes"""
        with self.assertRaises(ValueError):
            rec1 = Rectangle(-3, 7)
            rec2 = Rectangle(4, 0)
            rec3 = Rectangle(3, 5 -3, 2)
            rec4 = Rectangle(5, 3, 0, -1)

    def test_area(self):
        """test the area method"""
        self.assertEqual(Rectangle(4, 5).area(), 20)
        self.assertEqual(Rectangle(2, 1).area(), 2)
        self.assertEqual(Rectangle(20, 45).area(), 900)

    def test_display(self):
        """test the display method"""
        self.assertEqual(Rectangle(4, 5).display(), None)
        self.assertEqual(Rectangle(20, 45).display(), None)

    def test___str__(self):
        """test the __str__ method"""
        self.assertEqual(print(Rectangle(3, 5, 2, 1, 8)), None)
        self.assertEqual(print(Rectangle(2, 3)), None)
        self.assertEqual(print(Rectangle(3, 7, 2)), None)

    def test_update(self):
        """test the update method"""
        Rec1 = Rectangle(3, 5)
        Rec1.update(34)
        self.assertEqual(Rec1.id, 34)
        Rec2 = Rectangle(4, 7, 2, 4, 9)
        self.assertEqual(Rec2.id, 9)
        Rec2.update(14)
        self.assertEqual(Rec2.id, 14)
        Rec3 = Rectangle(4, 5, 2, 5, 8)
        self.assertEqual(Rec3.id, 8)
        self.assertEqual(Rec3.width, 4)
        self.assertEqual(Rec3.height, 5)
        self.assertEqual(Rec3.x, 2)
        self.assertEqual(Rec3.y, 5)
        Rec3.update(7, 4, 5, 1, 2)
        self.assertEqual(Rec3.id, 7)
        self.assertEqual(Rec3.width, 4)
        self.assertEqual(Rec3.height, 5)
        self.assertEqual(Rec3.x, 1)
        self.assertEqual(Rec3.y, 2)

    def test_update_kwargs(self):
        """test the update method for key-worded arguments"""
        Rec1 = Rectangle(1, 2, 3, 4, 5)
        Rec1.update(height=9)
        self.assertEqual(Rec1.height, 9)
        Rec1.update(8, 9, 10, 11, height=7)
        self.assertEqual(Rec1.id, 8)
        self.assertEqual(Rec1.width, 9)
        self.assertEqual(Rec1.height, 10)
        self.assertEqual(Rec1.x, 11)
        self.assertEqual(Rec1.y, 4)
        Rec1.update(width=3, id=4, y=5, x=6, height=7)
        self.assertEqual(Rec1.id, 4)
        self.assertEqual(Rec1.width, 3)
        self.assertEqual(Rec1.height, 7)
        self.assertEqual(Rec1.x, 6)
        self.assertEqual(Rec1.y, 5)

    def test_to_dictionary(self):
        """"test the public method to_dictionary"""
        Rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(Rec.to_dictionary(), {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5})
        Rec.update(6, 7, 8, 9, 10)
        self.assertEqual(Rec.to_dictionary(), {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10})
