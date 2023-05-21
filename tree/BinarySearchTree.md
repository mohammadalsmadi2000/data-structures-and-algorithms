## BinarySearchTree

The `BinarySearchTree` class is a subclass of the `BinaryTree` class and represents a binary search tree data structure. It inherits the basic functionality of a binary tree and provides additional methods for adding nodes and checking if a value exists in the tree.

### Problem Domain

The problem domain for the `BinarySearchTree` class is to efficiently store and search for values in a binary search tree. It should maintain the properties of a binary search tree, where the left child node has a value less than the parent node, and the right child node has a value greater than or equal to the parent node.

### Algorithm

The `BinarySearchTree` class adds the following methods to the `BinaryTree` class:

1. **add(value):** Adds a new node with the given value in the correct location in the binary search tree.
2. **contains(value):** Checks if the binary search tree contains a node with the given value.

The `add` method traverses the tree starting from the root and compares the value to be added with the values of the existing nodes to find the appropriate location. It recursively traverses the left or right subtree until it finds an empty spot for the new node.

The `contains` method also traverses the tree starting from the root. It compares the given value with the values of the existing nodes and recursively searches the left or right subtree until it finds the value or reaches a leaf node.

### Time Complexity Analysis

The time complexity of the `add` method depends on the height of the binary search tree. In the best case, where the tree is balanced, the height is approximately log(n), where n is the number of nodes. In the worst case, where the tree is skewed, the height can be equal to the number of nodes `n`.

- **add:** Best case: O(log(n)), Worst case: O(n)

The time complexity of the `contains` method is similar to the `add` method since it involves traversing the tree. It also depends on the height of the binary search tree.

- **contains:** Best case: O(log(n)), Worst case: O(n)

### Usage

You can create a `BinarySearchTree` object and use the provided methods to add nodes and check for values. For example:

```python
# Create a binary search tree
bst = BinarySearchTree()

# Add nodes to the tree
bst.add(10)
bst.add(5)
bst.add(15)

# Check if a value exists in the tree
contains_10 = bst.contains(10)  # Returns True
contains_7 = bst.contains(7)    # Returns False
