from .tree_data import root
from .traversal.preorder import preorder_traversal


def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


print("Inverted Binary Tree:")
root = invert_tree(root)
print(preorder_traversal(root))