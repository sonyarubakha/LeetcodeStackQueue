'''Maximum Frequency Stack task'''
from collections import defaultdict
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

class FreqStack:
    '''
    FreqStack class
    '''

    def __init__(self):
        '''
        Initializes freqstack using defaultdict.
        '''
        self.frequencies = defaultdict(int)
        self.stacks = defaultdict(Stack)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        '''
        pushes an integer val onto the top of the stack
        '''
        el = self.frequencies[val] + 1
        self.frequencies[val] = el
        if el > self.max_frequency:
            self.max_frequency = el
        self.stacks[el].push(val)

    def pop(self) -> int:
        '''
        removes and returns the most frequent element in the stack
        '''
        val = self.stacks[self.max_frequency].pop()
        self.frequencies[val] -= 1
        if self.stacks[self.max_frequency].is_empty():
            self.max_frequency -= 1
        return val
