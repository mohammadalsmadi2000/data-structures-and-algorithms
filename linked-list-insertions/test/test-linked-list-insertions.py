import pytest
from linkedlistinsertions.linkedlistinsertions import LinkedList


def test_linked_list():
    # Test append method
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1

    ll.append(2)
    assert ll.head.value == 1
    assert ll.head.next.value == 2

    ll.append(3)
    assert ll.head.value == 1
    assert ll.head.next.value == 2
    assert ll.head.next.next.value == 3

    # Test insert_before method
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    ll.insert_before(2, 5)
    assert ll.head.value == 1
    assert ll.head.next.value == 5
    assert ll.head.next.next.value == 2
    assert ll.head.next.next.next.value == 3

    ll.insert_before(1, 4)
    assert ll.head.value == 4
    assert ll.head.next.value == 1
    assert ll.head.next.next.value == 5
    assert ll.head.next.next.next.value == 2
    assert ll.head.next.next.next.next.value == 3

    ll.insert_before(3, 6)
    assert ll.head.value == 4
    assert ll.head.next.value == 1
    assert ll.head.next.next.value == 5
    assert ll.head.next.next.next.value == 2
    assert ll.head.next.next.next.next.value == 6
    assert ll.head.next.next.next.next.next.value == 3
