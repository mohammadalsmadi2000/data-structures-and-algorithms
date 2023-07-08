# Tree Intersection

## Problem Domain
Given two binary trees, find the values that are common in both trees.

## Visual

```
Tree 1               Tree 2
    1                    2
   / \                  / \
  2   3                3   4
 / \   \              /     \
4   5   6            5       6

Common Values: [3]
```


## Big O Analysis
The time complexity of the `tree_intersection` function is O(n + m), where n and m are the number of nodes in tree1 and tree2, respectively. This is because we need to traverse both trees to build the set of values and check for common values. The space complexity is O(n) since we store the values of tree1 in a set.

## Algorithm
1. Initialize an empty set `values1` to store the values of tree1.
2. Initialize an empty set `common_values` to store the common values between the trees.
3. Traverse tree1 and add its values to `values1` using a helper function:
   - If the current node is None, return.
   - Add the value of the current node to `values1`.
   - Recursively traverse the left subtree.
   - Recursively traverse the right subtree.
4. Check for common values in tree2 using another helper function:
   - If the current node is None, return.
   - If the value of the current node exists in `values1`, add it to `common_values`.
   - Recursively check for common values in the left subtree.
   - Recursively check for common values in the right subtree.
5. Return `common_values`.
## Code
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    values1 = set()
    common_values = set()

    def traverse_tree(node, values):
        if node is None:
            return
        values.add(node.value)
        traverse_tree(node.left, values)
        traverse_tree(node.right, values)

    traverse_tree(tree1, values1)

    def check_common_values(node):
        if node is None:
            return
        if node.value in values1:
            common_values.add(node.value)
        check_common_values(node.left)
        check_common_values(node.right)

    check_common_values(tree2)

    return common_values
