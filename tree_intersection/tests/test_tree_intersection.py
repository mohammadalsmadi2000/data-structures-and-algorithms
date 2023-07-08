# test_tree_intersection.py
from tree_intersection import TreeNode, tree_intersection

def test_tree_intersection():
    # Test case 1
    tree1 = TreeNode(150)
    tree1.left = TreeNode(100)
    tree1.right = TreeNode(250)
    tree1.left.left = TreeNode(75)
    tree1.left.right = TreeNode(160)
    tree1.right.left = TreeNode(200)
    tree1.right.right = TreeNode(350)
    tree1.left.left.right = TreeNode(125)
    tree1.right.left.left = TreeNode(175)
    tree1.right.right.left = TreeNode(300)
    tree1.right.right.right = TreeNode(500)

    tree2 = TreeNode(42)
    tree2.left = TreeNode(100)
    tree2.right = TreeNode(600)
    tree2.left.left = TreeNode(15)
    tree2.left.right = TreeNode(160)
    tree2.right.left = TreeNode(200)
    tree2.right.right = TreeNode(350)
    tree2.left.left.left = TreeNode(4)
    tree2.left.right.left = TreeNode(125)
    tree2.right.left.left = TreeNode(175)
    tree2.left.left.right = TreeNode(500)

    expected = [100, 160, 125, 175, 200, 350, 500]
    actual = tree_intersection(tree1, tree2)

    assert sorted(actual) == sorted(expected)
