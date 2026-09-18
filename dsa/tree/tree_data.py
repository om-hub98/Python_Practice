from .tree_node import Node


# Valid Binary Search Tree
#
#              10
#            /    \
#           8      16
#          / \    /  \
#         4   9  13  17
#        / \
#       2   6
#          / \
#         5   7


root = Node(10)

root.left = Node(8)
root.right = Node(16)

root.left.left = Node(4)
root.left.right = Node(9)

root.left.left.left = Node(2)
root.left.left.right = Node(6)

root.left.left.right.left = Node(5)
root.left.left.right.right = Node(7)

root.right.left = Node(13)
root.right.right = Node(17)