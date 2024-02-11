#!/usr/bin/python3
"""module
"""


class Node:
    """Node Class for singly linked list"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @data.setter
    def data(self, value):
        if not (type(value) is int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next.setter
    def next(self, value):
        if not (type(value) is Node):
            raise TypeError("next_node must be a Node object")
        self.__next = value


class SinglyLinkedList:
    """SLList Class"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        result = []
        curr = self.__head
        while curr is not None:
            result.append(str(curr.data))
            curr = curr.next
        return '\n'.join(result)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            curr = self.__head
            if new_node.data <= curr.data:
                new_node.next = curr
                self.__head = new_node
            else:
                while curr.next is not None:
                    if curr.next.data >= new_node.data:
                        new_node.next = curr.next
                        curr.next = new_node
                        break
                    curr = curr.next
                else:
                    curr.next = new_node
