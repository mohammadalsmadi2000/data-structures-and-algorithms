# Singly Linked List

## Summary
This is an implementation of a singly linked list data structure in Python. It includes a Node class with properties for the node's value and pointer to the next node, and a LinkedList class with a head property and methods for inserting a new node at the head, checking if a value exists in the list, and returning a string representation of the list.

## Description
A linked list is a linear data structure in which elements are stored in nodes that are linked together using pointers. Each node contains a value and a pointer to the next node in the list. In a singly linked list, each node can only point to the next node, while in a doubly linked list, each node points to both the next and previous nodes.

This implementation uses a singly linked list and provides methods for inserting nodes at the head of the list, checking if a value exists in the list, and returning a string representation of the list.

## Approach & Efficiency
The Node class has a constant time complexity of O(1) for creating a new node object. The LinkedList class has a constant time complexity of O(1) for creating a new empty linked list object.

The insert method of the LinkedList class has a constant time complexity of O(1) for inserting a new node at the head of the list.

The includes method of the LinkedList class has a linear time complexity of O(n) in the worst case, where n is the number of nodes in the list. This is because the method needs to traverse the list until it finds the value it's looking for or reaches the end of the list.

The to_string method of the LinkedList class also has a linear time complexity of O(n) in the worst case, because it needs to traverse the list and concatenate the string representation of each node.

## Solution

The solution consists of two classes:

1. Node: A class representing a node in the linked list, with properties for the node's value and pointer to the next node.

2. LinkedList: A class representing the linked list, with a head property and methods for inserting a new node at the head, checking if a value exists in the list, and returning a string representation of the list.

## Feature tasks for this challenge are completed
 * Create a Node class with properties for the value stored in the Node, and a pointer to the next Node.

 * Create a LinkedList class with a head property. Upon instantiation, an empty Linked List should be created.

 * Implement an insert method for the LinkedList class that adds a new node with a given value to the head of the list with an O(1) time performance.

 * Implement an includes method for the LinkedList class that indicates whether a given value exists as a node's value somewhere within the list. The method should have a linear time complexity of O(n) in the worst case.

 * Implement a to_string method for the LinkedList class that returns a string representing all the values in the linked list, formatted as "{ a } -> { b } -> { c } -> NULL".

 ## Unit tests written and passing
* "Can successfully instantiate an   empty linked list"
* "Can properly insert into the linked list"
* "The head property will properly point to the first node in the linked list"
* "Can properly insert multiple nodes into the linked list"
* "Will return true when finding a value within the linked list that exists"
* "Will return false when searching for a value in the linked list that does not exist"
* "Can properly return a collection of all the values that exist