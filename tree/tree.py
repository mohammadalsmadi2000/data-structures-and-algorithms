from collections import deque


class Node:
    def __init__(self, value):
        """
        Initialize a new node with the given value.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    """
    Represents a binary tree.

    Attributes:
        root (Node): The root node of the binary tree.
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order_traversal(self, start, traversal):
        """
        Performs a pre-order traversal of the binary tree.

        Args:
            start (Node): The starting node for traversal.
            traversal (list): The list to store the traversal results.

        Returns:
            list: The pre-order traversal of the binary tree.
        """
        if start:
            traversal.append(start.value)
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    def in_order_traversal(self, start, traversal):
        """
        Performs an in-order traversal of the binary tree.

        Args:
            start (Node): The starting node for traversal.
            traversal (list): The list to store the traversal results.

        Returns:
            list: The in-order traversal of the binary tree.
        """
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal.append(start.value)
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    def post_order_traversal(self, start, traversal):
        """
        Performs a post-order traversal of the binary tree.

        Args:
            start (Node): The starting node for traversal.
            traversal (list): The list to store the traversal results.

        Returns:
            list: The post-order traversal of the binary tree.
        """
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal.append(start.value)
        return traversal

    def find_maximum_value(self):
        if self.root is None:
            return None

        return self._find_maximum_value_recursive(self.root)

    def _find_maximum_value_recursive(self, current_node):
        if current_node is None:
            return float('-inf')

        max_value = current_node.value
        left_max = self._find_maximum_value_recursive(current_node.left)
        right_max = self._find_maximum_value_recursive(current_node.right)

        if left_max > max_value:
            max_value = left_max

        if right_max > max_value:
            max_value = right_max

        return max_value
    
    def breadth_first(self):
        """
        Performs a breadth-first traversal of the binary tree and returns a list of values encountered.

        Returns:
            list: A list of values encountered in the tree in the order they were encountered.
        """
        if not self.root:
            return []

        traversal = []
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            traversal.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return traversal


class BinarySearchTree(BinaryTree):
    """
    Represents a binary search tree, a subclass of BinaryTree.

    Methods:
        add(value): Adds a new node with the given value to the binary search tree.
        contains(value): Checks if the binary search tree contains a node with the given value.

    Inherited Methods:
        pre_order_traversal(start, traversal): Performs a pre-order traversal of the binary tree.
        in_order_traversal(start, traversal): Performs an in-order traversal of the binary tree.
        post_order_traversal(start, traversal): Performs a post-order traversal of the binary tree.
    """

    def __init__(self, root=None):
        super().__init__(root)

    def add(self, value):
        """
        Adds a new node with the given value in the correct location in the binary search tree.

        Args:
            value: The value to be added to the binary search tree.
        """
        if not self.root:
            self.root = Node(value)
        else:
            self._add_helper(self.root, value)

    def _add_helper(self, node, value):
        """
        A helper method for the add method.

        Recursively finds the correct location to add the new node in the binary search tree.

        Args:
            node (Node): The current node being examined.
            value: The value to be added to the binary search tree.
        """
        if value < node.value:
            if node.left:
                self._add_helper(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add_helper(node.right, value)
            else:
                node.right = Node(value)

    def contains(self, value):
        """
        Checks if the binary search tree contains a node with the given value.

        Args:
            value: The value to be checked.

        Returns:
            bool: True if the value exists in the binary search tree, False otherwise.
        """
        return self._contains_helper(self.root, value)

    def _contains_helper(self, node, value):
        """
        A helper method for the contains method.

        Recursively searches for the value in the binary search tree.

        Args:
            node (Node): The current node being examined.
            value: The value to be searched.

        Returns:
            bool: True if the value exists in the binary search tree, False otherwise.
        """
        if not node:
            return False

        if node.value == value:
            return True
        elif value < node.value:
            return self._contains_helper(node.left, value)
        else:
            return self._contains_helper(node.right, value)
    



# Testing the functionality of BinaryTree
# Test 1: Can successfully instantiate an empty tree
empty_tree = BinaryTree()
assert empty_tree.root is None

# Test 2: Can successfully instantiate a tree with a single root node
single_node_tree = BinaryTree(Node(1))
assert single_node_tree.root.value == 1

# Test 3: For a Binary Search Tree, can successfully add a left child and right child properly to a node
bst_tree = BinaryTree(Node(10))
bst_tree.root.left = Node(5)
bst_tree.root.right = Node(15)
assert bst_tree.root.left.value == 5
assert bst_tree.root.right.value == 15


# Test 4: Can successfully return a collection from a pre-order traversal
pre_order_traversal = bst_tree.pre_order_traversal(bst_tree.root, [])
assert pre_order_traversal == [10, 5, 15]

# Test 5: Can successfully return a collection from an in-order traversal
in_order_traversal = bst_tree.in_order_traversal(bst_tree.root, [])
assert in_order_traversal == [5, 10, 15]

# Test 6: Can successfully return a collection from a post-order traversal
post_order_traversal = bst_tree.post_order_traversal(bst_tree.root, [])
assert post_order_traversal == [5, 15, 10]


# Testing the functionality of BinarySearchTree
# Test 1: Can successfully instantiate an empty tree
empty_tree = BinarySearchTree()
assert empty_tree.root is None

# Test 2: Can successfully instantiate a tree with a single root node
single_node_tree = BinarySearchTree(Node(1))
assert single_node_tree.root.value == 1

# Test 3: For a Binary Search Tree, can successfully add a left child and right child properly to a node
bst_tree = BinarySearchTree()
bst_tree.add(10)
bst_tree.add(5)
bst_tree.add(15)
assert bst_tree.root.value == 10
assert bst_tree.root.left.value == 5
assert bst_tree.root.right.value == 15

# Test 4: Can successfully return a collection from a pre-order traversal
pre_order_traversal = bst_tree.pre_order_traversal(bst_tree.root, [])
assert pre_order_traversal == [10, 5, 15]

# Test 5: Can successfully return a collection from an in-order traversal
in_order_traversal = bst_tree.in_order_traversal(bst_tree.root, [])
assert in_order_traversal == [5, 10, 15]

# Test 6: Can successfully return a collection from a post-order traversal
post_order_traversal = bst_tree.post_order_traversal(bst_tree.root, [])
assert post_order_traversal == [5, 15, 10]

# Test 7: Returns True for the contains method, given an existing node value
assert bst_tree.contains(10) is True
assert bst_tree.contains(5) is True
assert bst_tree.contains(15) is True

# Test 8: Returns False for the contains method, given a non-existing node value
assert bst_tree.contains(3) is False
assert bst_tree.contains(20) is False


# All tests passed
print("Code Challenge 15 Test , All tests passed!")

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


# Create a binary tree
tree = BinaryTree(Node(2))
tree.root.left = Node(7)
tree.root.right = Node(5)
tree.root.left.left = Node(2)
tree.root.left.right = Node(6)
tree.root.right.right = Node(9)
tree.root.left.right.left = Node(5)
tree.root.left.right.right = Node(11)
tree.root.right.right.left = Node(4)

result = tree.breadth_first()
print("breadth first :",result)