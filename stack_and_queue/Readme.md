# Problem Domain:
Implement a stack and a queue data structure using a linked list.

# Visual:

![1_zKnDkJpL-4GQ36kzrDiODQ](https://user-images.githubusercontent.com/60603704/236282981-5ee36791-3402-48ba-812a-391fb53fcbb8.png)

# Algorithm:
### For the Stack:
* push(value):

1. Create a new Node with the specified value.
2. Set the next pointer of the new Node to the current top of the stack.
3. Set the top of the stack to the new Node.

* pop():

1. Check if the stack is empty. If it is, raise an exception.
2. Get the value of the Node at the top of the stack.
3. Set the top of the stack to the next Node.
4. Return the value of the Node.


* peek():

1. Check if the stack is empty. If it is, raise an exception.
2. Return the value of the Node at the top of the stack.


* is_empty():

1. Check if the top of the stack is None. If it is, return True. Otherwise, return False.

### For the Queue:

* enqueue(value):

1. Create a new Node with the specified value.
2. If the queue is empty, set both the front and the back of the queue to the new Node.
3. Otherwise, set the next pointer of the current back of the queue to the new Node, and set the back of the queue to the new Node.

* dequeue():

1. Check if the queue is empty. If it is, raise an exception.
2. Get the value of the Node at the front of the queue.
3. Set the front of the queue to the next Node.
4. If the front of the queue is now None, set the back of the queue to None as well.
5. Return the value of the Node.


* peek():

1. Check if the queue is empty. If it is, raise an exception.
2. Return the value of the Node at the front of the queue.


* is_empty():

1. Check if the front of the queue is None. If it is, return True. Otherwise, return False.

# Big O:
### For the Stack:

push(): O(1)
pop(): O(1)
peek(): O(1)
is_empty(): O(1)


### For the Queue:

enqueue(): O(1)
dequeue(): O(1)
peek(): O(1)
is_empty(): O(1)


# Pseudocode:
```
Stack:
push(value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node

pop():
    if self.is_empty():
        raise Exception("Stack is empty")
    value = self.top.value
    self.top = self.top.next
    return value

peek():
    if self.is_empty():
        raise Exception("Stack is empty")
    return self.top.value

is_empty():
    return self.top is None


Queue:
enqueue(value):
    new_node = Node(value)
    if self.is_empty():
        self.front = new_node
    else:
        self.back.next = new_node
    self.back = new_node

dequeue():
    if self.is_empty():
        raise Exception("Queue is empty")
    value = self.front.value
    self.front = self.front.next
    if self.front is None:
        self.back = None
    return value

peek():
    if self.is_empty():
        raise Exception

```