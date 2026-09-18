from .tree_data import root

def find_depth(root):
    if root is None:
        return 0

    left_depth = find_depth(root.left)
    right_depth = find_depth(root.right)

    return 1 + max(left_depth, right_depth)
    
print("Depth of the tree:")
print(find_depth(root))