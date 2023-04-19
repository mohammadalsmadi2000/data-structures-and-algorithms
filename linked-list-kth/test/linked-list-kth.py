import pytest
from linkedlistkth.linkedlistkth import LinkedList,Node
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
        ll.kth_from_end(-1)
    except ValueError as e:
        assert str(e) == "k must be a positive integer"  # k is not a positive integer

    # Test kth_from_end method with linked list of size greater than 1
    ll.head.next = Node(3)
    ll.head.next.next = Node(8)
    ll.head.next.next.next = Node(2)
    assert ll.kth_from_end(0) == 2  # k is 0
    assert ll.kth_from_end(2) == 3  # k is less than length of linked list
    try:
        ll.kth_from_end(6)
    except ValueError as e:
        assert str(e) == "k is greater than the length of the linked list"  # k is greater than length of linked list
    try:
        ll.kth_from_end(-1)
    except ValueError as e:
        assert str(e) == "k must be a positive integer"  # k is not a positive integer
    assert ll.kth_from_end(3) == 1  # k is equal to length of linked list
    assert ll.kth_from_end(1) == 8  # k is somewhere in the middle of linked list

    # Test find_middle method
    ll.head = Node(1)
    assert ll.find_middle() == 1  # linked list size is 1
    ll.head.next = Node(3)
    ll.head.next.next = Node(8)
    ll.head.next.next.next = Node(2)
    assert ll.find_middle() == 8  # linked list size is even
    ll.head.next.next.next.next = Node(5)
    assert ll.find_middle() == 8  # linked list size is odd
    ll.head.next.next.next.next.next = Node(9)
    assert ll.find_middle() == 3  # linked list size is odd
    ll.head.next.next.next.next.next.next = Node(7)
    assert ll.find_middle() == 2  # linked list size is even
