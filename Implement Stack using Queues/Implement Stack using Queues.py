class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty queue")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.rear = None
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.head.val

    def __len__(self):
        return self.size

class MyStack:

    def __init__(self):
        self.q_1 = Queue()
        self.q_2 = Queue()

    def push(self, x: int) -> None:
        self.q_2.push(x)
        while not self.q_1.is_empty():
            self.q_2.push(self.q_1.pop())
        self.q_1, self.q_2 = self.q_2, self.q_1

    def pop(self) -> int:
        return self.q_1.pop()

    def top(self) -> int:
        return self.q_1.peek()

    def empty(self) -> bool:
        return self.q_1.is_empty()
