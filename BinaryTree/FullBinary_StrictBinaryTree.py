'''
FULL BINARY TREE:
Each node has exactly 2 children or none and leaf node can be at different level.
                1
              /   \
             2     3
            / \   / \
           4   5 6   7

STRICT BINARY TREE(PROPER BINARY TREE):
Each node has either 0 or 2 children except leaf node
                1
              /   \
             2     3
                  / \
                 6   7

Note: 
1. Also sometimes referred to as either a strict tree or proper tree.
2. A strict binary tree is always a full binary tree, but a full binary tree is not necessarily strict unless all nodes have exactly 2 children or none.
'''


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_full_binary_tree(root):
    if root is None:
        return True
    # if a node has one child, its not a full binary tree
    if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        return False
    return is_full_binary_tree(root.left) and is_full_binary_tree(root.right)

def is_strict_binary_tree(root):
    if root is None:
        return True
    # if the node has exactly two children, check recursively
    if root.left and root.right:
        return is_strict_binary_tree(root.left) and is_strict_binary_tree(root.right)
    
    # if its a leaf node (no children), its valid
    if root.left is None and root.right is None:
        return True
    
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

'''
                1
              /   \
             2     3
            / \   / \
           4   5 6   7


'''
print("Is full binary tree? ", is_full_binary_tree(root))
print("Is strict binary tree? ", is_strict_binary_tree(root))

'''
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
          /
         8 
        

'''
root.left.left.left = Node(8)
print("Is full binary tree? ", is_full_binary_tree(root))
print("Is strict binary tree? ", is_strict_binary_tree(root))


'''
                1
              /   \
             2     3
            / \   / \
           4   5 6   7
          / \
         8   9
        

'''

root.left.left.right = Node(9)
print("Is full binary tree? ", is_full_binary_tree(root))
print("Is strict binary tree? ", is_strict_binary_tree(root))
