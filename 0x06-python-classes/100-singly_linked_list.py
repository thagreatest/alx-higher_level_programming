#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = Node(value, self.__head)  # we initialize a new node
            return None
        if value < self.__head.data:  # if new data is less, it is new head
            self.__head = Node(value, self.__head)
            return None
        # then if the data is greather
        new_node = self.__head
        while new_node.next_node and new_node.next_node.data < value:
            """ while there is a next node and that data is less, then next """
            new_node = new_node.next_node
        new_node.next_node = Node(value, new_node.next_node)

    def __str__(self):
        if not self.__head:
            return ""
        temp = self.__head
        string = ""
        while temp is not None:
            try:
                string += str(temp.data)
                temp = temp.next_node
                string += "\n"
            except:
                pass
        return string[:-1]
