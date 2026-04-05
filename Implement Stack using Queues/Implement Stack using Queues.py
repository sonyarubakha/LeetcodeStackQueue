'''Implement Stack using Queues task'''
class Node:
    '''
    Node class.
    '''
    def __init__(self, val, next=None):
        '''
        Initializes the node.
        '''
        self.val = val
        self.next = next

class Queue:
    '''
    Queue class.
    '''
    def __init__(self):
        '''
        Initializes the queue.
        '''
        self.head = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        '''
        Returns true if the queue is empty, false otherwise.
        '''
        return self.head is None

    def push(self, item):
        '''
        Pushes element to the back of the queue
        '''
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def pop(self):
        '''
        Removes the element from the front
        of the queue and returns it.
        '''
        if self.is_empty():
            raise IndexError
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.rear = None
        return val

    def peek(self):
        '''
        Returns the element at the front of the queue.
        '''
        if self.is_empty():
            raise IndexError
        return self.head.val

    def __len__(self):
        '''
        Returns the size of the queue.
        '''
        return self.size

class MyStack:
    '''
    Stack class.
    '''

    def __init__(self):
        '''
        Initializes two queues for stack.
        '''
        self.q_1 = Queue()
        self.q_2 = Queue()

    def push(self, x: int) -> None:
        '''
        Pushes element x to the top of the stack.
        '''
        self.q_2.push(x)
        while not self.q_1.is_empty():
            self.q_2.push(self.q_1.pop())
        self.q_1, self.q_2 = self.q_2, self.q_1

    def pop(self) -> int:
        '''
        Removes the element on the top of the stack and returns it.
        '''
        return self.q_1.pop()

    def top(self) -> int:
        '''
        Returns the element on the top of the stack.
        '''
        return self.q_1.peek()

    def empty(self) -> bool:
        '''
        Returns true if the stack is empty, false otherwise.
        '''
        return self.q_1.is_empty()
