#!/usr/bin/python3

class Node:
    """Node class for a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a Node with given data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List class"""

    def __init__(self):
        """Initialize an empty singly linked list"""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return string representation of the singly linked list"""
        if self.head is None:
            return ""
        current = self.head
        result = str(current.data)
        while current.next_node is not None:
            current = current.next_node
            result += "\n" + str(current.data)
        return result


if __name__ == "__main__":
    SinglyLinkedList = SinglyLinkedList()

    SinglyLinkedList.sorted_insert(2)
    SinglyLinkedList.sorted_insert(5)
    SinglyLinkedList.sorted_insert(3)
    SinglyLinkedList.sorted_insert(10)
    SinglyLinkedList.sorted_insert(1)
    SinglyLinkedList.sorted_insert(-4)
    SinglyLinkedList.sorted_insert(-3)
    SinglyLinkedList.sorted_insert(4)
    SinglyLinkedList.sorted_insert(5)
    SinglyLinkedList.sorted_insert(12)
    SinglyLinkedList.sorted_insert(3)

    print(SinglyLinkedList)

