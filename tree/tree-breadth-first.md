# Breadth First 

## Problem Domain

Given a binary tree, we need to traverse it in a breadth-first manner and return a list of all values encountered in the order they were encountered.

## Visual
```
Example Binary Tree:

        2
       / \
      7   5
     / \   \
    2   6   9
       / \   \
      5   11  4
             

Breadth-First Traversal: [2, 7, 5, 2, 6, 9, 5, 11, 4]
```
## Algorithm

1. Create an empty `traversal` list to store the values encountered.
2. Create an empty queue data structure.
3. Enqueue the root node of the binary tree.
4. Repeat the following steps while the queue is not empty:
     - Dequeue a node from the front of the queue.
     - Append the value of the dequeued node to the `traversal` list.
     - Enqueue the left child of the dequeued node if it exists.
     - Enqueue the right child of the dequeued node if it exists.
5. Return the `traversal` list.


## Time Complexity
The time complexity of the `breadth_first` function is O(n), where n is the number of nodes in the binary tree. This is because each node is visited exactly once during the breadth-first traversal.

The enqueue and dequeue operations have a time complexity of O(1) since they are implemented using a queue data structure.

Therefore, the overall time complexity of the `breadth_first` function is O(n).

## Space Complexity
The space complexity of the `breadth_first` function is O(n) as well. This is because the queue data structure is used to store the nodes during traversal, and in the worst case, all the nodes in the binary tree can be present in the queue at a certain point.

Therefore, the overall space complexity of the `breadth_first` function is O(n).
## Pseudocode

```python
function breadth_first(tree):
    traversal = []
    queue = createQueue()
    enqueue(queue, tree.root)
    
    while not isEmpty(queue):
        node = dequeue(queue)
        append(traversal, node.value)
        
        if node.left:
            enqueue(queue, node.left)
        if node.right:
            enqueue(queue, node.right)
    
    return traversal

```