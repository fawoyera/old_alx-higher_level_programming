#!/usr/bin/python3
"""Module that defines a base class"""
import json
import csv
from turtle import *


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to return JSON string represent of list of dict"""
        if (list_dictionaries is None) or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method to write JSON string represent of list_objs to file"""
        list_objs_dict = []
        if list_objs is not None:
            list_objs_dict = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as fp:
            fp.write(Base.to_json_string(list_objs_dict))

    @staticmethod
    def from_json_string(json_string):
        """static method to return dictionary represent of JSON string"""
        if (json_string is None) or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method to return instance of class with all attributes set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method to load instance of class from JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as fp:
                return [cls.create(**dict) for dict in (cls.from_json_string(fp.read()))]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method to write CSV represent of list_objs to file"""
        list_objs_dict = []
        if list_objs is not None:
            list_objs_dict = [obj.to_dictionary() for obj in list_objs]
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        with open(filename, "w", newline='') as fp:
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writerows(list_objs_dict)

    @classmethod
    def load_from_file_csv(cls):
        """class method to load instance of class from CSV file"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == 'Rectangle':
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        else:
            fieldnames = ['id', 'size', 'x', 'y']
        try:
            with open(filename, "r", newline='') as fp:
                return [cls.create(**dicti) for dicti in [{k: int(v) for k, v in dict.items()} for dict in csv.DictReader(fp, fieldnames=fieldnames)]]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """static method to draw rectangles and squares to GUI"""
        list_rec_dict = [rec.to_dictionary() for rec in list_rectangles]
        list_sq_dict = [sq.to_dictionary() for sq in list_squares]

        color('blue')
        up()
        for rec in list_rec_dict:
            home()
            forward(rec['x'])
            left(90)
            forward(rec['y'])
            right(90)
            down()
            forward(rec['width'])
            left(90)
            forward(rec['height'])
            left(90)
            forward(rec['width'])
            left(90)
            forward(rec['height'])
            left(90)
            up()

        color('green')
        for sq in list_sq_dict:
            home()
            forward(sq['x'])
            left(90)
            forward(sq['y'])
            right(90)
            down()
            forward(sq['size'])
            left(90)
            forward(sq['size'])
            left(90)
            forward(sq['size'])
            left(90)
            forward(sq['size'])
            left(90)
            up()
