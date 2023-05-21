# Binary Tree Traversal

This project provides an implementation of a binary tree and various traversal methods to visit the nodes in different orders. The binary tree supports preorder, inorder, and postorder traversals, while a binary search tree subclass also includes methods for adding nodes and checking if a value exists in the tree.

## Problem Domain
A binary tree is a data structure in which each node can have at most two children: a left child and a right child. Traversal of a binary tree involves visiting each node exactly once in a specific order. The three common types of binary tree traversals are:

- Preorder: Visit the current node, then recursively visit the left subtree, and finally recursively visit the right subtree.
- Inorder: Recursively visit the left subtree, then visit the current node, and finally recursively visit the right subtree.
- Postorder: Recursively visit the left subtree, then recursively visit the right subtree, and finally visit the current node.

A binary search tree is a special type of binary tree in which the nodes are ordered based on their values. The left child of a node contains a value less than the parent node, and the right child contains a value greater than the parent node.

## visual 

### `Binary Tree`
![tree_1_qw3am1](https://github.com/mohammadalsmadi2000/data-structures-and-algorithms/assets/60603704/9ba852ac-322d-41d9-bc25-435c154d215d)
### `Binary Search Trees`
![download](https://github.com/mohammadalsmadi2000/data-structures-and-algorithms/assets/60603704/f6beb91f-46b5-4084-b9ae-4bcc79e472b7)


## Algorithm

The binary tree implementation consists of two classes: `Node` and `BinaryTree`. The `Node` class represents a node in the tree with a value, left child, and right child. The `BinaryTree` class represents the binary tree and provides methods for preorder, inorder, and postorder traversals. These traversal methods use recursive helper functions to visit the nodes in the desired order.

The binary search tree implementation extends the `BinaryTree` class and adds additional methods for adding nodes and checking if a value exists in the tree. The `add` method recursively finds the correct position to insert a new node based on its value. The `contains` method recursively searches the tree to check if a given value exists in any of the nodes.

## Big O Analysis

The time complexity of the binary tree traversal methods (preorder, inorder, and postorder) is O(n), where n is the number of nodes in the tree. This is because each node needs to be visited exactly once.

The time complexity of adding a node to a binary search tree using the `add` method depends on the structure of the tree. In the worst case, when the tree is unbalanced and resembles a linked list, the time complexity is O(n), where n is the number of nodes in the tree. However, in the average case or when the tree is balanced, the time complexity is O(log n), as the tree's structure allows for efficient insertion.

The time complexity of checking if a value exists in a binary search tree using the `contains` method also depends on the structure of the tree. In the worst case, when the tree is unbalanced, the time complexity is O(n), as all nodes need to be visited to search for the value. In the average case or when the tree is balanced, the time complexity is O(log n), as the search can be efficiently narrowed down to a subtree.

The space complexity of the binary tree and binary search tree implementations is O(n), where n is the number of nodes in the tree. This is because recursive calls and the resulting call stack consume memory proportional to the height of the tree, which can be up to n in the worst case.
