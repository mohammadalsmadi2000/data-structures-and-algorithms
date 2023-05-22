## Problem Domain
Given a binary tree with numeric values, we need to find the maximum value stored in the tree.

## Algorithm
1. Initialize the `find_maximum_value` method.
2. Check if the tree has a root node. If not, return `None` to indicate an empty tree.
3. Call the `_find_maximum_value_recursive` method with the root node as the starting point.
4. In the `_find_maximum_value_recursive` method:
   - If the current node is `None`, return negative infinity to indicate an empty subtree.
   - Initialize `max_value` with the value of the current node.
   - Recursively call `_find_maximum_value_recursive` for the left subtree and store the result in `left_max`.
   - Recursively call `_find_maximum_value_recursive` for the right subtree and store the result in `right_max`.
   - If `left_max` is greater than `max_value`, update `max_value` with `left_max`.
   - If `right_max` is greater than `max_value`, update `max_value` with `right_max`.
   - Return the `max_value`.
5. Return the result obtained from `_find_maximum_value_recursive` as the maximum value of the tree.

## Big O Complexity
The time complexity of the `find_maximum_value` method is O(n), where n is the number of nodes in the binary tree. This is because we need to visit each node once to find the maximum value. The space complexity is O(h), where h is the height of the binary tree. This is due to the recursive calls on the stack, which can go up to the height of the tree.

## Test Case
```python
# Create a binary tree with numeric values
tree = BinaryTree()
tree.root = Node(2)
tree.root.left = Node(7)
tree.root.right = Node(5)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.right.left = Node(9)
tree.root.right.right = Node(11)

# Test the find_maximum_value method
maximum_value = tree.find_maximum_value()
print("Maximum value:", maximum_value)

```
## Output 
```
Maximum value: 11
```
