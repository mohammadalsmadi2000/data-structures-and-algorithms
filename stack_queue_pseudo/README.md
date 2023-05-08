# Problem Domain
The goal of this project is to implement a queue data structure using two stacks. A queue is a collection of elements that supports adding elements to the back of the collection (enqueue) and removing elements from the front of the collection (dequeue). A stack is a collection of elements that supports adding elements to the top of the collection (push) and removing elements from the top of the collection (pop).

# Visual

```
Enqueue 10:   stack1: [10]
Enqueue 15:   stack1: [10, 15]
Enqueue 20:   stack1: [10, 15, 20]

Dequeue:      stack1: [], stack2: [20, 15]

```

# Algorithm
Here's a step-by-step algorithm for the enqueue method:

1. Push the value onto the top of stack1.


Here's a step-by-step algorithm for the dequeue method:

1. If both stack1 and stack2 are empty, there's nothing to dequeue, so return None.
2. If stack2 is empty, pop all items from stack1 and push them onto stack2, effectively reversing the order of the items.
3. Pop and return the top item from stack2.


# Big O
The time complexity of enqueue method is O(1) because it simply pushes the value onto the top of stack1.

The time complexity of dequeue method is O(n) in the worst case because it may need to pop all items from stack1 and push them onto stack2, which takes O(n) time, where n is the number of items in the queue.

The space complexity of the PseudoQueue class is O(n), where n is the maximum number of items that will be stored in the queue at any given time. This is because the two stacks used to implement the queue may each store up to n items.