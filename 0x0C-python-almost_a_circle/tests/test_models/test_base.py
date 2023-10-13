#!/usr/bin/python3
"""Test module for base class"""
import unittest, sys, csv
sys.path.insert(0, './models/')
from base import Base
from rectangle import Rectangle
from square import Square


class TestBase(unittest.TestCase):
    """Test Class"""
    def test_attr(self):
        """test if class attribute is private"""
        with self.assertRaises(AttributeError):
            m = Base.__nb_objects
            n = Base().__nb_objects

    def test_init(self):
        """test initialization of class instance attribute"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(9).id, 9)
        self.assertEqual(Base(-4).id, -4)
        self.assertEqual(Base(0).id, 0)

    def test_to_json_string(self):
        """test the static method to_json_string of class Base"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        Rec = Rectangle(3, 4, 7, 5, 10)
        Rec_dict = Rec.to_dictionary()
        self.assertEqual(Rec_json := Base.to_json_string([Rec_dict]), '[{"id": 10, "width": 3, "height": 4, "x": 7, "y": 5}]')
        self.assertTrue(type(Rec_dict) is dict)
        self.assertTrue(type(Rec_json) is str)
        Rec1 = Rectangle(4, 5)
        Rec1.update(9, 7, 3, 2, 1)
        Rec1_dict = Rec1.to_dictionary()
        Rec2 = Rectangle(3, 4, 5)
        Rec2.update(4, 2, 1, 6, 7)
        Rec2_dict = Rec2.to_dictionary()
        self.assertEqual(Rec2_json := Base.to_json_string([Rec1_dict, Rec2_dict]), '[{"id": 9, "width": 7, "height": 3, "x": 2, "y": 1}, {"id": 4, "width": 2, "height": 1, "x": 6, "y": 7}]')
        self.assertTrue(type(Rec2_dict) is dict)
        self.assertTrue(type(Rec2_json) is str)

    def test_save_to_file(self):
        """test the class method save_to_file of class Base"""
        self.assertEqual(Base.save_to_file(None), None)
        with open("Base.json", "r") as fp:
            self.assertEqual(fp.read(), '[]')
        Rec = Rectangle(4, 5, 4, 3, 7)
        self.assertEqual(Rectangle.save_to_file([Rec]), None)
        with open("Rectangle.json", "r") as fp:
            self.assertEqual(fp.read(), '[{"id": 7, "width": 4, "height": 5, "x": 4, "y": 3}]')
        Sq1 = Square(5, 7, 3, 1)
        Sq2 = Square(4, 9, 1, 2)
        self.assertEqual(Square.save_to_file([Sq1, Sq2]), None)
        with open("Square.json", "r") as fp:
            self.assertEqual(fp.read(), '[{"id": 1, "size": 5, "x": 7, "y": 3}, {"id": 2, "size": 4, "x": 9, "y": 1}]')

    def test_from_json_string(self):
        """test the static method from_json_string of class Base"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        json_string = '[{"id": 4, "width": 5, "height": 2, "x": 1, "y": 0}]'
        self.assertEqual(json_dict := Base.from_json_string(json_string), [{'id': 4, 'width': 5, 'height': 2, 'x': 1, 'y': 0}])
        self.assertTrue(type(json_string) is str)
        self.assertTrue(type(json_dict[0]) is dict)
        json_string_2 = '[{"id": 1, "width": 2, "height": 3}, {"x": 5, "y": 6}]'
        self.assertEqual(json_dict_2 := Base.from_json_string(json_string_2), [{'id': 1, 'width': 2, 'height': 3}, {'x': 5, 'y': 6}])
        self.assertTrue(type(json_string_2) is str)
        self.assertTrue(type(json_dict_2[0]) is dict)

    def test_create(self):
        """test the class method create of the Base class"""
        self.assertTrue((type(rec := Rectangle.create(**{'id': 3, 'width': 5, 'height': 7}))).__name__ == 'Rectangle')
        self.assertTrue((type(sq := Square.create(**{'id': 3, 'size': 9}))).__name__ == 'Square')
        self.assertTrue(isinstance(rec, Rectangle))
        self.assertTrue(isinstance(sq, Square))

    def test_load_from_file(self):
        """test the class method load_from_file of the Base class"""
        self.assertEqual(Base.load_from_file(), [])

        with open("Rectangle.json", "w") as fp:
            fp.write('[{"id": 1, "width": 3, "height": 5}, {"id": 2, "width": 7, "height": 4}]')
        self.assertTrue(type(rec := Rectangle.load_from_file()).__name__ == 'list')
        self.assertTrue(isinstance(rec[0], Rectangle))

        with open("Square.json", "w") as fp:
            fp.write('[{"id": 4, "size": 9}, {"id": 9, "size": 3}, {"id": 3, "size": 4}]')
        self.assertTrue(type(sq := Square.load_from_file()).__name__ == 'list')
        self.assertTrue(isinstance(sq[0], Square))

    def test_save_to_file_csv(self):
        """test the class method save_to_file_csv of the Base class"""
        self.assertEqual(Base.save_to_file_csv(None), None)

        fieldnames = ['id']
        with open("Base.csv", "r", newline='') as fp:
            self.assertEqual([row for row in csv.DictReader(fp, fieldnames=fieldnames)], [])

        Rec = Rectangle(4, 5, 4, 3, 7)
        self.assertEqual(Rectangle.save_to_file_csv([Rec]), None)
        fieldnames = ['id', 'width', 'height', 'x', 'y']
        with open("Rectangle.csv", "r", newline='') as fp:
            self.assertEqual([row for row in csv.DictReader(fp, fieldnames=fieldnames)], [{"id": '7', "width": '4', "height": '5', "x": '4', "y": '3'}])
        
        Sq1 = Square(5, 7, 3, 1)
        Sq2 = Square(4, 9, 1, 2)
        self.assertEqual(Square.save_to_file_csv([Sq1, Sq2]), None)
        fieldnames = ['id', 'size', 'x', 'y']
        with open("Square.csv", "r", newline='') as fp:
            self.assertEqual([row for row in csv.DictReader(fp, fieldnames=fieldnames)], [{"id": '1', "size": '5', "x": '7', "y": '3'}, {"id": '2', "size": '4', "x": '9', "y": '1'}])

    def test_load_from_file_csv(self):
        """test the class method load_from_file_csv of the Base class"""
        self.assertEqual(Base.load_from_file_csv(), [])

        with open("Rectangle.csv", "w", newline='') as fp:
            fieldnames = ['id', 'width', 'height', 'x', 'y']
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writerows([{"id": 1, "width": 3, "height": 5, "x": 0, "y": 0}, {"id": 2, "width": 7, "height": 4, "x": 0, "y": 0}])
        self.assertTrue(type(rec := Rectangle.load_from_file_csv()).__name__ == 'list')
        self.assertTrue(isinstance(rec[0], Rectangle))

        with open("Square.csv", "w", newline='') as fp:
            fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writerows([{"id": 4, "size": 9, "x": 0, "y": 0}, {"id": 9, "size": 3, "x": 0, "y": 0}, {"id": 3, "size": 4, "x": 0, "y": 0}])
        self.assertTrue(type(sq := Square.load_from_file_csv()).__name__ == 'list')
        self.assertTrue(isinstance(sq[0], Square))
