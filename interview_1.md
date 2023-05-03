#  Reverse Singly Linked List

## Problem Domain
Given a singly linked list, write a function to reverse the order of the list. The function should reverse the pointers of each node in the list so that the last node becomes the head node and the second to last node becomes the next node of the head node, and so on.

## Visual

Before:
```
head -> 1 -> 2 -> 3 -> 4 -> 5 -> None

```
After:
```
head -> 5 -> 4 -> 3 -> 2 -> 1 -> None

```

## Algorithm

1. Set current to the head of the linked list.
2. Initialize prev to None and next_node to None.
3. Traverse the linked list using the current pointer.
4. In each iteration, store the next node of the current node in next_node.
5. Set the next node of the current node to the prev node.
6. Set prev node to the current node.
7. Set current node to the next node.
8. Repeat until the current node is None.
9. Set the head of the linked list to the prev node.

## Big O
The time complexity of this algorithm is O(n) because it iterates through the linked list once. The space complexity is O(1) because it uses a constant amount of extra space to store the prev and next_node pointers.

## Pseudocode

```
reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head

```
## Code:
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self):
        if self.head is None:
            return "None"
        else:
            linked_list = []
            current = self.head
            while current is not None:
                linked_list.append(str(current.data))
                current = current.next
            linked_list.append("None")
            return "->".join(linked_list)

# Example usage
linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)
print(linked_list) # Output: 1->2->3->4->5->None
linked_list.reverse_linked_list()
print(linked_list) # Output: 5->4->3->2->1->None

```


## Test
```
def test_reverse_linked_list():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)
    linked_list.add_node(5)
    assert str(linked_list) == "1->2->3->4->5->None"
    linked_list.reverse_linked_list()
    assert str(linked_list) == "5->4->

```
