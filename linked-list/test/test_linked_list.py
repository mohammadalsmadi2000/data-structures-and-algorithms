import pytest
from linkedlist.linkedlist  import Node, LinkedList

def test_insert():
    ll = LinkedList()
    ll.insert(1)
    assert ll.head.value == 1
    ll.insert(2)
    assert ll.head.value == 2

def test_includes():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.includes(2) == True
    assert ll.includes(4) == False

def test_to_string():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.to_string() == "{ 3 } -> { 2 } -> { 1 } -> NULL"

def test_empty_list():
    ll = LinkedList()
    assert ll.head == None

def test_multiple_inserts():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    assert ll.to_string() == "{ 3 } -> { 2 } -> { 1 } -> NULL"
    assert ll.includes(1) == True
    assert ll.includes(4) == False