class Node:
    def __init__(self, value):
        """
        Initialize a new node with the given value.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root = None

    def preorder_traversal(self):
        """
        Perform a preorder traversal of the binary tree.
        Returns a list of values in the traversal order.
        """
        result = []
        if self.root:
            self.preorder(self.root, result)
        return result

    def preorder(self, node, result):
        """
        Helper function for preorder traversal.
        """
        result.append(node.value)
        if node.left:
            self.preorder(node.left, result)
        if node.right:
            self.preorder(node.right, result)

    def inorder_traversal(self):
        """
        Perform an inorder traversal of the binary tree.
        Returns a list of values in the traversal order.
        """
        result = []
        if self.root:
            self.inorder(self.root, result)
        return result

    def inorder(self, node, result):
        """
        Helper function for inorder traversal.
        """
        if node.left:
            self.inorder(node.left, result)
        result.append(node.value)
        if node.right:
            self.inorder(node.right, result)

    def postorder_traversal(self):
        """
        Perform a postorder traversal of the binary tree.
        Returns a list of values in the traversal order.
        """
        result = []
        if self.root:
            self.postorder(self.root, result)
        return result

    def postorder(self, node, result):
        """
        Helper function for postorder traversal.
        """
        if node.left:
            self.postorder(node.left, result)
        if node.right:
            self.postorder(node.right, result)
        result.append(node.value)


class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Add a new node with the given value to the binary search tree.
        The node is inserted in the correct location based on the value.
        """
        if not self.root:
            self.root = Node(value)
        else:
            self.add_helper(self.root, value)

    def add_helper(self, node, value):
        """
        Helper function for adding a node to the binary search tree.
        """
        if value < node.value:
            if node.left:
                self.add_helper(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.add_helper(node.right, value)
            else:
                node.right = Node(value)

    def contains(self, value):
        """
        Check if the binary search tree contains a node with the given value.
        Returns True if the value is found, False otherwise.
        """
        if self.root:
            return self.contains_helper(self.root, value)
        return False

    def contains_helper(self, node, value):
        """
        Helper function for checking if a value is contained in the binary search tree.
        """
        if node.value == value:
            return True
        elif value < node.value and node.left:
            return self.contains_helper(node.left, value)
        elif value > node.value and node.right:
            return self.contains_helper(node.right, value)
        return False


# Testing the functionality
# Instantiate an empty tree
tree = BinarySearchTree()

# Instantiate a tree with a single root node
tree.root = Node(5)

# Add left and right children to the root node
tree.root.left = Node(3)
tree.root.right = Node(7)

# Add values to the tree
tree.add(1)
tree.add(4)
tree.add(6)
tree.add(9)

# Perform traversals
print("Preorder Traversal:", tree.preorder_traversal())  # [5, 3, 1, 4, 7, 6, 9]
print("Inorder Traversal:", tree.inorder_traversal())    # [1, 3, 4, 5, 6, 7, 9]
print("Postorder Traversal:", tree.postorder_traversal())  # [1, 4, 3, 6, 9, 7, 5]

# Test the 'contains' method
print("Contains 6:", tree.contains(6))  # True
print("Contains 2:", tree.contains(2))  # False
