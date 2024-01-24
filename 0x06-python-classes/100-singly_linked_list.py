#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""100-singly_linked_list.py

This module contains an implementation of a singly linked list in python3

"""


class Node(object):
    """Represents a single node of a singly linked list having data, and a
    pointer/reference to the next node of the list
    """

    def __init__(self, data, next_node=None):
        """Initialaizes a newly created Node instance.

        Args:
            data (int): The data held by the node
            next_node (Node): Reference to the next node of the list

        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        """Returns a user friendly string representationof a Node instance."""
        return "data: {}\nnext_node: {}".format(self.__data,
                                                type(self.__next_node))

    @property
    def data(self):
        """Getter and setter pair for the private data attribute.

        Setter also performs type validation of the given value/data.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        if value.__class__ != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter and setter pair for the private next_node attribute.

        Setter also performs type validation of the given value.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and value.__class__ != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList(object):
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a newly created SinglyLinkedList instance/object."""
        self.__head = None

    def __str__(self):
        """Returns a user friendly string representation of an instance."""

        output = ""
        node_ptr = self.__head
        while node_ptr is not None:
            output += "{:d}".format(node_ptr.data)
            node_ptr = node_ptr.next_node
            if node_ptr is not None:
                output += '\n'
        return (output)

    def sorted_insert(self, value):
        """Inserts a new node (Node instance) to a SinglyLinkedList instance
        into the correct position (the list is sorted in increasing order).

        Args:
            value (int): The value to be held by the Node instance.

        """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node_ptr = self.__head
            while (node_ptr.next_node is not None and
                   node_ptr.next_node.data < value):
                node_ptr = node_ptr.next_node
            new_node.next_node = node_ptr.next_node
            node_ptr.next_node = new_node
