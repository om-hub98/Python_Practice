from ..tree_data import root

# Postorder Traversal -> Left-Right-Root

def postorder_traversal(root):
    if root is None:
        return 

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")


print("Postorder Traversal:")
postorder_traversal(root)
