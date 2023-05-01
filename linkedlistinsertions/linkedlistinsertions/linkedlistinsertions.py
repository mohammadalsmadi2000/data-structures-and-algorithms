class Node:
    """
    Represents a single node of a linked list.
    
    Attributes:
        value (Any): The value of the node.
        next (Node): The reference to the next node.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a singly linked list data structure.
    
    Attributes:
        head (Node): The reference to the first node of the list.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.
        
        Args:
            value (Any): The value to be added to the list.
        """
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
        """
        Inserts a new node with the given value before the node with the specified value.
        
        Args:
            value (Any): The value of the existing node.
            new_value (Any): The value of the new node to be inserted.
        
        Raises:
            Exception: If the list is empty or the specified value is not found.
        """
        if not self.head:
            raise Exception("List is empty")

        if self.head.value == value:
            new_node = Node(new_value)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise Exception(f"Node with value {value} not found")

    def insert_after(self, value, new_value):
        """
        Inserts a new node with the given value after the node with the specified value.
        
        Args:
            value (Any): The value of the existing node.
            new_value (Any): The value of the new node to be inserted.
        
        Raises:
            Exception: If the list is empty or the specified value is not found.
        """
        if not self.head:
            raise Exception("List is empty")

        current = self.head
        while current:
            if current.value == value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise Exception(f"Node with value {value} not found")

    def delete(self, value):
        """
        Deletes the first node with the specified value from the list.
        
        Args:
            value (Any): The value of the node to be deleted.
        
        Raises:
            Exception: If the list is empty or the specified value is not found.
        """
        if not self.head:
            raise Exception("List is empty")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

        raise Exception(f"Node with value {value} not found")
