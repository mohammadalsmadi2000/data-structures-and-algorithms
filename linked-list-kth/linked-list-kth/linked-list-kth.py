class LinkedList:
    def __init__(self):
        """Initializes an empty linked list with a null head"""
        self.head = None

    def kth_from_end(self, k):
        """
        Takes an integer k as input and returns the value of the node that is k places from the tail of the linked list.

        Args:
            k (int): The index of the node from the tail of the linked list.

        Returns:
            int: The value of the node that is k places from the tail of the linked list.

        Raises:
            ValueError: If k is less than 0 or greater than the length of the linked list.
        """
        if k < 0:
            raise ValueError("k must be a positive integer")

        p1 = self.head
        p2 = self.head

        for i in range(k):
            if p1 is None:
                raise ValueError("k is greater than the length of the linked list")
            p1 = p1.next

        if p1 is None:
            return self.head.value

        while p1.next is not None:
            p1 = p1.next
            p2 = p2.next

        return p2.value

    def find_middle(self):
        """
        Returns the value of the node at the middle of the linked list.

        Returns:
            int: The value of the node at the middle of the linked list.

        """
        if self.head is None:
            return None

        p1 = self.head
        p2 = self.head

        while p1 is not None and p1.next is not None:
            p1 = p1.next.next
            p2 = p2.next

        return p2.value
