from ..tree_data import root

'''
# BST - Binary Search Tree
Tree should be sorted in the give order-
Left < Root < Right
- means : left side of the tree will have values less than root 
        and right side of the tree will have values greater than root.


Apply Inorder Traversal for searching.
'''

def binary_search(root, search_val)-> bool:
    if root is None:
        return False

    if root.data == search_val:
        return True

    if search_val < root.data:
       return binary_search(root.left, search_val)

    return binary_search(root.right, search_val)


print("Binary Search on Tree :")
print(binary_search(root, 14))