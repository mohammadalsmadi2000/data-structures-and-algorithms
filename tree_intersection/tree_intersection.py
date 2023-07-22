from Hash.hash import Hashtable
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root, values):

    if root is not None:
        in_order_traversal(root.left, values)
        values.append(root.value)
        in_order_traversal(root.right, values)

def tree_intersection(tree1, tree2):
   
    values1 = []
    in_order_traversal(tree1, values1)

    values2 = []
    in_order_traversal(tree2, values2)

    set1 = set(values1)
    set2 = set(values2)

    intersection = set()
    hashtable = Hashtable()

    for value in set1:
        if hashtable.get(value) is None:
            hashtable.set(value, 1)

    for value in set2:
        if hashtable.get(value) is not None:
            intersection.add(value)

    return intersection
