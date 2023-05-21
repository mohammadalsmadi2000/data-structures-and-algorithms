## BinaryTree

The `BinaryTree` class represents a binary tree data structure. It allows for the creation of a binary tree and provides methods for performing depth-first traversals: pre-order, in-order, and post-order.

### Problem Domain

The problem domain for the `BinaryTree` class is to efficiently store and traverse a binary tree. The class should have properties for the value stored in each node, as well as the left and right child nodes.

### Algorithm

1. **Pre-order traversal:** Visit the root, then traverse the left subtree, and finally traverse the right subtree.
2. **In-order traversal:** Traverse the left subtree, visit the root, and then traverse the right subtree.
3. **Post-order traversal:** Traverse the left subtree, traverse the right subtree, and finally visit the root.

### Time Complexity Analysis

The time complexity of each traversal method depends on the number of nodes in the binary tree. Let `n` be the number of nodes.

- **Pre-order traversal:** O(n)
- **In-order traversal:** O(n)
- **Post-order traversal:** O(n)

These traversal methods have to visit each node exactly once, resulting in a time complexity of O(n).

### Space Complexity Analysis

The space complexity of each traversal method depends on the height of the binary tree. In the worst case, where the binary tree is skewed, the height can be equal to the number of nodes `n`.

- **Pre-order traversal:** O(n)
- **In-order traversal:** O(n)
- **Post-order traversal:** O(n)

The space complexity is determined by the recursive calls made during the traversal, which can be as deep as the height of the tree.

### Usage

You can create a `BinaryTree` object and perform the desired traversal by calling the corresponding method. For example:

```python
# Create a binary tree
binary_tree = BinaryTree()

# Perform pre-order traversal
pre_order_result = binary_tree.pre_order_traversal(binary_tree.root, [])

# Perform in-order traversal
in_order_result = binary_tree.in_order_traversal(binary_tree.root, [])

# Perform post-order traversal
post_order_result = binary_tree.post_order_traversal(binary_tree.root, [])
