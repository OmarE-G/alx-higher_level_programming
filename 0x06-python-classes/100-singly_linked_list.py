#!/usr/bin/python3
"""module
"""


class Node:
    """Node Class for singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not (type(value) is int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not (type(value) in [Node, type(None)]):
            raise TypeError("next_node_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SLList Class"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        result = []
        curr = self.__head
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.next_node
        return '\n'.join(result)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            curr = self.__head
            if new_node.data <= curr.data:
                new_node.next_node = curr
                self.__head = new_node
            else:
                while curr.next_node is not None:
                    if curr.next_node.data >= new_node.data:
                        new_node.next_node = curr.next_node
                        curr.next_node = new_node
                        break
                    curr = curr.next_node
                else:
                    curr.next_node = new_node
