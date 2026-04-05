class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        self.head = Node(item, next=self.head)
        self.size += 1

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            raise IndexError
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.head.val

    def __len__(self):
        return self.size

    def __str__(self):
        if self.is_empty():
            return 'Stack is empty.'
        el = []
        now = self.head
        while now:
            el.append(str(now.val))
            now = now.next
        el = el[::-1]
        return f"bottom -> {' '.join(el)} <- top"

class MyQueue:

    def __init__(self):
        self.stk_1 = Stack()
        self.stk_2 = Stack()

    def push(self, x: int) -> None:
        self.stk_1.push(x)

    def pop(self) -> int:
        if self.stk_2.is_empty():
            while not self.stk_1.is_empty():
                self.stk_2.push(self.stk_1.pop())
        return self.stk_2.pop()

    def peek(self) -> int:
        if self.stk_2.is_empty():
            while not self.stk_1.is_empty():
                self.stk_2.push(self.stk_1.pop())
        return self.stk_2.peek()

    def empty(self) -> bool:
        return self.stk_1.is_empty() and self.stk_2.is_empty()
