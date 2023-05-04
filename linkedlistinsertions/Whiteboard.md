# linked list insertions

# Problem Domain#
We are asked to implement three methods for the Linked List class: append, insert before, and insert after. The append method should add a new node with the given value to the end of the list. The insert before method should add a new node with the given new value immediately before the first node that has the value specified. The insert after method should add a new node with the given new value immediately after the first node that has the value specified.

## Visual
![1_ey_yx2nxH_6-PcQHazTg6A](https://user-images.githubusercontent.com/60603704/232413055-3c62c751-8b3c-4cb0-84c2-b734cfeccc1f.gif)

## Algorithm

1. append method:
* Check if the linked list is empty, if so, make the new node the head of the list
* Otherwise, traverse the linked list to the end
* Set the next pointer of the last node to the new node
2. insert before method:
* Traverse the linked list until a node with the value specified is found
* If the value is not found, throw an exception
* Otherwise, create a new node with the given new value
* Set the next pointer of the new node to the node with the value specified
* Set the next pointer of the previous node to the new node
3. insert after method:
* Traverse the linked list until a node with the value specified is found
* If the value is not found, throw an exception
* Otherwise, create a new node with the given new value
* Set the next pointer of the new node to the next node of the node with the value specified
* Set the next pointer of the node with the value specified to the new node

## Big O
1. append method:
* Time Complexity: O(n)
* Space Complexity: O(1)
2. insert before method:
* Time Complexity: O(n)
* Space Complexity: O(1)
3. insert after method:
* Time Complexity: O(n)
* Space Complexity: O(1)

## Pseudocode
1. append method:
```
1. Create a new Node object with the given value.
2. If the list is empty, set head to the new node.
3. Otherwise, traverse the list to find the last node.
4. Set the last node's next property to the new node.

```
```
insert before method:

1. Create a new Node object with the given new value.
2. If the list is empty, raise an exception.
3. If the node to insert before is the head node, set head to the new node and set the new node's next property to the original head node.
4. Otherwise, traverse the list to find the node with the given value.
5. If the node is not found, raise an exception.
6. Set the new node's next property to the found node and set the previous node's next property to the new node.

```

```
insert after method:
1. Create a new Node object with the given new value.
2. If the list is empty, raise an exception.
3. Traverse the list to find the node with the given value.
4. If the node is not found, raise an exception.
5. Set the new node's next property to the found node's next property.
6. Set the found node's next property to the new node.

```
```
delete(value)
1. If the list is empty, raise an exception.
2. If the node to delete is the head node, set head to the head's next node and return.
3. Traverse the list to find the node with the given value.
4. If the node is not found, raise an exception.
5. Set the previous node's next property to the found node's next property.

```

## Code:
```
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
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


```

## Test
```
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

```