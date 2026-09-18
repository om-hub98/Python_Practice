from ..tree_data import root

# Preorder Traversal -> Root-Left-Right

def preorder_traversal(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


print("Preorder Traversal:")
preorder_traversal(root)