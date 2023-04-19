# Linked List Kth Node

## Problem Domain

Implement a method for the LinkedList class that returns the value of the node that is k places from the tail of the linked list.

## Visual

Let's say we have a linked list with the following values: 1 -> 3 -> 8 -> 2 -> 5 -> 7 -> 4. If we call the kth_from_end method with k=2, the method should return 5, which is 2 places from the tail of the linked list.

```
1 -> 3 -> 8 -> 2 -> 5 -> 7 -> 4
          ^              ^
          |              |
          k=2            tail

```

## Algorithm
To implement the kth_from_end method, we can use two pointers, p1 and p2, initialized to point to the head of the linked list. We first move p1 k steps forward, so that it is k nodes ahead of p2. Then we move both p1 and p2 forward one node at a time until p1 reaches the tail of the linked list. At this point, p2 should be pointing to the node that is k places from the tail of the linked list.

## Big O

The time complexity of the kth_from_end method is O(n), where n is the length of the linked list. We need to iterate through the linked list twice, once to find its length and once to find the kth node from the end.

The space complexity of the kth_from_end method is O(1). We only need to use a constant amount of extra space to store the two pointers.

## Pseudocode

```
kth_from_end(k):
    if k < 0:
        raise ValueError("k must be a positive integer")
    p1 = head
    p2 = head
    for i in range(k):
        if p1 is None:
            raise ValueError("k is greater than the length of the linked list")
        p1 = p1.next
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2.value

```

## Code

```
class LinkedList:
    def __init__(self):
        self.head = None

    def kth_from_end(self, k):
        if k < 0:
            raise ValueError("k must be a positive integer")
        p1 = self.head
        p2 = self.head
        for i in range(k):
            if p1 is None:
                raise ValueError("k is greater than the length of the linked list")
            p1 = p1.next
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next
        return p2.value

```
## Test

```
def test_linked_list():
    ll = LinkedList()

    # Test kth_from_end method
    ll.head = Node(1)
    assert ll.kth_from_end(0) == 1  # k is 0 and length of linked list is 1
    try:
        ll.kth_from_end(1)
    except ValueError as e:
        assert str(e) == "k is greater than the length of the linked list"  # k is greater than length of linked list
    try:
        ll.kth_from_end(-1

```