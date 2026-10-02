from ..tree_data import root

# Inorder Traversal -> Left-Root-Right

def inorder_traversal(root)-> list[int]:

    result = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        result.append(node.data)
        inorder(node.right)

    inorder(root)
    return result

print("Inorder Traversal:")
print(inorder_traversal(root))