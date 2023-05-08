class Stack:
    """
    A class representing a stack data structure.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the top of the stack."""
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.
        Return None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Return the top item from the stack without removing it.
        Return None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.items[-1]


class PseudoQueue:
    """
    A class representing a queue data structure implemented using two stacks.
    """

    def __init__(self):
        """
        Initialize the PseudoQueue with two empty stacks, stack1 and stack2.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """
        Add a value to the end of the queue.
        This is done by pushing the value onto stack1.
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        Remove and return the value at the front of the queue.
        This is done by popping all items from stack1 and pushing them onto stack2,
        effectively reversing the order of the items.
        The top item of stack2 is then popped and returned, which is the oldest item that was originally added to the queue.
        """
        if self.stack1.is_empty() and self.stack2.is_empty():
            # Both stacks are empty, there's nothing to dequeue
            return None

        if self.stack2.is_empty():
            # stack2 is empty, so we need to move items from stack1 to stack2
            while not self.stack1.is_empty():
                # Pop an item from stack1 and push it onto stack2
                self.stack2.push(self.stack1.pop())

        # Pop and return the top item from stack2
        return self.stack2.pop()

if __name__ == '__main__':
    pq = PseudoQueue()

    pq.enqueue(10)
    pq.enqueue(15)
    pq.enqueue(20)