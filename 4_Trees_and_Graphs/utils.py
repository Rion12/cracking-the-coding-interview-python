from random import randint

class Node:

    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)

class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.length = 0
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        values = ', '.join(values)
        return values

    def append_right(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.length += 1

    def append_left(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.length += 1

    def add_multiple(self, values):
        for v in values:
            self.append_right(v)

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.append_right(randint(min_value, max_value))
        return self

    def peek(self):
        return self.tail.value

    def display(self):
        print(self)

class DoublyLinkedList(LinkedList):

    def append_right(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        self.length += 1

    def append_left(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head.prev = Node(value, self.head, None)
            self.head = self.head.prev
        self.length += 1

    def pop(self):
        if self.head.value == self.tail.value:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
