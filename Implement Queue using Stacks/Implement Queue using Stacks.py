'''Implement Queue using Stacks task.'''
class Node:
    '''
    Node class.
    '''
    def __init__(self, val, next=None):
        '''
        Initializes node.
        '''
        self.val = val
        self.next = next

class Stack:
    '''
    Stack class.
    '''
    def __init__(self):
        '''
        Initializes the stack.
        '''
        self.head = None
        self.size = 0

    def push(self, item):
        '''
        Adds element to the top of the stack.
        '''
        self.head = Node(item, next=self.head)
        self.size += 1

    def is_empty(self):
        '''
        Checks if stack is empty.
        '''
        return self.head is None

    def pop(self):
        '''
        Deletes top element from the stack
        and returns it.
        '''
        if self.is_empty():
            raise IndexError
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def peek(self):
        '''
        Returns the top element.
        '''
        if self.is_empty():
            raise IndexError
        return self.head.val

    def __len__(self):
        '''
        Returns size of a stack.
        '''
        return self.size

    def __str__(self):
        '''
        String info about the stack
        '''
        if self.is_empty():
            return 'Stack is empty.'
        res = ''
        now = self.head
        while now:
            if res == '':
                res = str(now.val)
            else:
                res = str(now.val) + ' ' + res
            now = now.next
        return f"bottom -> {res} <- top"

class MyQueue:
    '''
    Queue class.
    '''

    def __init__(self):
        '''
        Initializes two stacks for queue.
        '''
        self.stk_1 = Stack()
        self.stk_2 = Stack()

    def push(self, x: int) -> None:
        '''
        Pushes element x to the back of the queue
        '''
        self.stk_1.push(x)

    def pop(self) -> int:
        '''
        Removes the element from the front
        of the queue and returns it.
        '''
        if self.stk_2.is_empty():
            while not self.stk_1.is_empty():
                self.stk_2.push(self.stk_1.pop())
        return self.stk_2.pop()

    def peek(self) -> int:
        '''
        Returns the element at the front of the queue.
        '''
        if self.stk_2.is_empty():
            while not self.stk_1.is_empty():
                self.stk_2.push(self.stk_1.pop())
        return self.stk_2.peek()

    def empty(self) -> bool:
        '''
        Returns true if the queue is empty, false otherwise.
        '''
        return self.stk_1.is_empty() and self.stk_2.is_empty()
