#!/usr/bin/python3
"""Module to create a singly linked list"""


class Node:
    """Class that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Method to initialize the singly linked list"""
        try:
            assert type(data) == int
        except Exception:
            raise TypeError('data must be an integer')
        else:
            self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Method to retrieve the data in a node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Method to set the value of data in a node"""
        try:
            assert type(value) == int
        except Exception:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Method to retrieve the next_node" of linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Method to set the value of the next_node in a linked list"""
        try:
            assert type(value) == Node or value is None
        except Exception:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class to define a singly linked lists"""
    def __init__(self):
        """Method to initialize a singly linked list"""
        self.__head = None
        temp = self.__head

    def __str__(self):
        """Method to pretty print the linked list"""
        temp = self.__head
        result = ""
        while (temp):
            result += str(temp.data) + '\n'
            temp = temp.next_node
        result = result[:-1]
        return result

    def sorted_insert(self, value):
        """Method that inserts a new Node into correct sorted position"""
        temp = self.__head

        new = Node(value)
        if temp is None or temp.data >= value:
            new.next_node = self.__head
            self.__head = new
            return
        else:
            while (temp):
                if temp.next_node is None:
                    new.next_node = None
                    temp.next_node = new
                    return
                if temp.next_node.data < value:
                    temp = temp.next_node
                else:
                    new.next_node = temp.next_node
                    temp.next_node = new
                    return
