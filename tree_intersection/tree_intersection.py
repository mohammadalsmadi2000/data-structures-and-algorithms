class TreeNode:
    """
    Represents a node in a binary tree.
    """
    def __init__(self, value):
        """
        Initializes a new instance of the TreeNode class.

        Args:
            value: The value of the node.
        """
        self.value = value
        self.left = None
        self.right = None


def tree_intersection(tree1, tree2):
    """
    Finds the common values in two binary trees.

    Args:
        tree1: The root node of the first binary tree.
        tree2: The root node of the second binary tree.

    Returns:
        A set of values found in both trees.
    """
    values1 = set()
    common_values = set()

    def traverse_tree(node, values):
        """
        Traverses the binary tree and adds its values to the set.

        Args:
            node: The current node being traversed.
            values: The set to store the values.
        """
        if node is None:
            return
        values.add(node.value)
        traverse_tree(node.left, values)
        traverse_tree(node.right, values)

    traverse_tree(tree1, values1)

    def check_common_values(node):
        """
        Checks if each value of the second tree exists in the first tree's values set.

        Args:
            node: The current node being checked.
        """
        nonlocal common_values
        if node is None:
            return
        if node.value in values1:
            common_values.add(node.value)
        check_common_values(node.left)
        check_common_values(node.right)

    check_common_values(tree2)

    return common_values
