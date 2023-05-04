class Node:
    """A class representing a node in a linked list."""
    def __init__(self, value):
        """
        Initializes a new instance of the Node class with the specified value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None

class Stack:
    """A class representing a stack data structure implemented using a linked list."""

    def __init__(self):
        """Initializes a new instance of the Stack class."""
        self.top = None

    def push(self, value):
        """
        Adds a new node with the specified value to the top of the stack.

        Args:
            value: The value to be added to the stack.

        Time Complexity: O(1)
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """
        Removes the node from the top of the stack and returns its value.

        Returns:
            The value of the node from the top of the stack.

        Raises:
            Exception: If the stack is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Returns the value of the node located at the top of the stack.

        Returns:
            The value of the node located at the top of the stack.

        Raises:
            Exception: If the stack is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Returns a boolean indicating whether or not the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.

        Time Complexity: O(1)
        """
        return self.top is None

class Queue:
    def __init__(self):
        """A class representing a queue data structure implemented using a linked list."""
        self.front = None
        self.back = None

    def enqueue(self, value):
        """
        Adds a new node with the specified value to the back of the queue.

        Args:
            value: The value to be added to the queue.

        Time Complexity: O(1)
        """
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node

    def dequeue(self):
        """
        Removes the node from the front of the queue and returns its value.

        Returns:
            The value of the node from the front of the queue.

        Raises:
            Exception: If the queue is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.back = None
        return value

    def peek(self):
        """
        Returns the value of the node located at the front of the queue.

        Returns:
            The value of the node located at the front of the queue.

        Raises:
            Exception: If the queue is empty.

        Time Complexity: O(1)
        """
        if self.is_empty():
         
            raise Exception("Queue is empty")
        return self.front.value

    def is_empty(self):
        """
        Returns a boolean indicating whether or not the queue is
        
        Returns:
        True if the queue is empty, False otherwise.

        Time Complexity: O(1)
        """
        return self.front is None
