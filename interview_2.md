# Palindrome

## Problem Domain:
We are given a singly linked list, and we need to write a function to validate whether or not it's a palindrome. A palindrome linked list is a list that reads the same backward as forward.

## Visual:
Here's an example of a palindrome linked list:
head -> 1 -> 2 -> 3 -> 2 -> 1 -> null
The above linked list reads the same backward as forward.

## Algorithm:

1. Initialize two pointers, slow and fast to the head of the linked list.
2. Traverse the linked list using the fast pointer which moves two steps at a time.
3. When the fast pointer reaches the end of the linked list, the slow pointer would have reached the middle of the linked list.
4. Reverse the second half of the linked list.
5. Traverse the first half of the linked list and the reversed second half of the linked list in parallel, and compare each node.
6. If all nodes are equal, return true, else return false.

## Big O:
The time complexity of the above algorithm is O(n) where n is the number of nodes in the linked list. The space complexity of the algorithm is O(1) as we only use constant extra space.

## Pseudocode:

```
function isPalindrome(head):
    if head is null or head.next is null:
        return true

    # Initialize two pointers
    slow = head
    fast = head

    # Traverse the linked list
    while fast.next is not null and fast.next.next is not null:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = null
    current = slow.next
    while current is not null:
        next = current.next
        current.next = prev
        prev = current
        current = next

    # Traverse the first half and the reversed second half of the linked list in parallel and compare each node
    secondHalf = prev
    firstHalf = head
    while secondHalf is not null:
        if firstHalf.value != secondHalf.value:
            return false
        firstHalf = firstHalf.next
        secondHalf = secondHalf.next

    return true

```

## Code:
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Initialize two pointers
    slow = head
    fast = head

    # Traverse the linked list
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev = None
    current = slow.next
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    # Traverse the first half and the reversed second half of the linked list in parallel and compare each node
    second_half = prev
    first_half = head
    while second_half is not None:
        if first_half.value != second_half.value:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

```

## Test:
```
# The linked list is a palindrome
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
assert is_palindrome(head) == True
```
