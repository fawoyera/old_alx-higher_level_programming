#!/usr/bin/python3
"""Module that defines a student with public instance attributes"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Ïnitialization method for student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """"Method to retrieve dict representation of student instance"""
        return self.__dict__
