#!/usr/bin/python3
"""Module that defines a student with public instance attributes"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Ïnitialization method for student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"Method to retrieve dict representation of student instance"""
        if (type(attrs) == list) and all(type(item) == str for item in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
