# linked-list

## Problem Domain:
We want to implement a linked list data structure that allows us to insert new nodes at the beginning of the list, check if a value exists in the list, and display the list as a string.

## Visual
![1_ey_yx2nxH_6-PcQHazTg6A](https://user-images.githubusercontent.com/60603704/232413055-3c62c751-8b3c-4cb0-84c2-b734cfeccc1f.gif)


## Algorithm:
We will define two classes, Node and LinkedList, to implement the linked list data structure. The Node class will represent each node in the linked list, and the LinkedList class will represent the linked list itself.

* insert(value): This method will take a value as an argument and insert a new node with that value at the beginning of the linked list.
* includes(value): This method will take a value as an argument and return True if the linked list contains a node with that value, and False otherwise.
* to_string(): This method will return a string representation of the linked list.

## Big O:

* insert(value): The time complexity of this method is O(1), as we are only adding a new node at the beginning of the list, and the number of operations does not depend on the size of the list.
* includes(value): The time complexity of this method is O(n), as we may have to traverse the entire list to check if a node with the given value exists.
* to_string(): The time complexity of this method is also O(n), as we have to traverse the entire list to create the string representation.

## Pseudocode:

```
Node:
- __init__(self, value): Initialize a new Node object with a given value and a null next pointer.

LinkedList:
- __init__(self): Initialize a new LinkedList object with a null head pointer.
- insert(self, value): Create a new Node with the given value and set its next pointer to the current head of the LinkedList. Set the head of the LinkedList to the new Node.
- includes(self, value): Start at the head of the LinkedList and traverse through the list until a node with the given value is found, or until the end of the list is reached. Return True if a node with the value is found, and False otherwise.
- to_string(self): Start at the head of the LinkedList and traverse through the list, appending each node's value to a string with "->" in between. Append "NULL" to the end of the string and return it.
```

## Code:


```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        result = ""
        current = self.head
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result

```
## Test:
```
# Test case 1
list = LinkedList()
list.insert(10)
list.insert(20)
list.insert(30)
list.insert(40)

assert list.includes(10) == True
assert list.includes(20) == True
assert list.includes(30) == True
assert list.includes(40) == True
assert list.includes(50) == False

assert str(list.to_string()) == "{{ 40 }} -> {{ 30 }} -> {{ 20 }} -> {{ 10 }} -> NULL"

```
