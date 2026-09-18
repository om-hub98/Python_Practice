from ..tree_data import root

# Inorder Traversal -> Left-Root-Right

def inorder_traversal(root):

    if root is None:
        return

    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)

print("Inorder Traversal:")
inorder_traversal(root)  