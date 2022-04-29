# Make Stack iterable
class Stack:
    def __init__(self, top=None):
        self.top = top

    def __iter__(self):
        def value_generator():
            current = self.top
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def push(self, value):
        node = Node(value)
        if self.is_empty():
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack!")
        else:
            popped = self.top
            self.top = popped.next
            popped.next = None
            return popped.value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack!")
        else:
            return self.top.value

    def is_empty(self):
        return self.top == None

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next