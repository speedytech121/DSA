'''
Complete Binary Tree is a special type of binary tree where all the levels of the tree are filled completely except the lowest level nodes, which are filled from as left as possible.

                1
              /   \
             2     3
            / \   / 
           4   5 6   

PROPERTIES:
* A complete binary tree is said to be a proper binary tree where all leaves have the same depth.
* In a complete binary tree number of nodes at depth d is 2d. 
* In a  complete binary tree with n nodes height of the tree is log(n+1).
* All the levels except the last level are completely full.         


PERFECT BINARY TREE VS COMLETE BINARY TREE:
A binary tree of height ‘h’ having the maximum number of nodes is a perfect binary tree. 
For a given height h, the maximum number of nodes is 2h+1-1.

A complete binary tree of height h is a perfect binary tree up to height h-1, and in the last level element are stored in left to right order.

Example 1:
                1
              /   \
             2     3
            / \   / \
           4   5 6   7

The height of the given binary tree is 2 and the maximum number of nodes in that tree is n= 2h+1-1 =  22+1-1 =  23-1 = 7.
Hence we can conclude it is a perfect binary tree.
Now for a complete binary tree, It is full up to height h-1 i.e.; 1, and the last level elements are stored in left to right order. 
Hence it is a complete Binary tree also. Here is the representation of elements when stored in an array


Example 2:
                1
              /   \
             2     3
            / \   / 
           4   5 6   

Height of the given binary tree is 2 and the maximum number of nodes that should be there are 2h+1 – 1 = 22+1 – 1 = 23 – 1 = 7. 
But the number of nodes in the tree is 6. Hence it is not a perfect binary tree.
Now for a complete binary tree, It is full up to height h-1 i.e.; 1, and the last level element are stored in left to right order. 
Hence this is a complete binary tree. Store the element in an array and it will be like;

'''


'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# function to count total nodes in the tree
def count_nodes(root):
    if root is None:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)

# function to check if the tree is a complete binary tree
def is_complete_binary_tree(root, index = 0, node_count = None):
    if root is None:
        return True
    if node_count is None:
        node_count = count_nodes(root)
    
    # if index exceeds the total node count, its not complete
    if index>=node_count:
        return False
    
    # recursively check left and right subtrees
    return (is_complete_binary_tree(root.left, 2*index+1, node_count) and is_complete_binary_tree(root.right, 2*index+2 , node_count))

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("Is Complete Binary Tree?", is_complete_binary_tree(root))  # Output: True

# Adding an extra node to the right (breaks CBT rule)
root.right.right = Node(7)
print("Is Complete Binary Tree after modification?", is_complete_binary_tree(root))  # Output: False'
'''

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to count total nodes in the tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Function to check if the tree is a Complete Binary Tree
def is_complete_binary_tree(root, index=0, node_count=None):
    if root is None:
        return True
    
    if node_count is None:
        node_count = count_nodes(root)

    # If index exceeds the total node count, it's not complete
    if index >= node_count:
        return False

    # Recursively check left and right subtrees
    return (is_complete_binary_tree(root.left, 2 * index + 1, node_count) and
            is_complete_binary_tree(root.right, 2 * index + 2, node_count))

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
print("Is Complete Binary Tree?", is_complete_binary_tree(root))  # Output: True
'''
                1
              /   \
             2     3
            / \   / 
           4   5 6   
'''
# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)
# Adding an extra node to the right (breaks CBT rule)
root.right.right = Node(7)

print("Is Complete Binary Tree after modification?", is_complete_binary_tree(root))  # Output: False
'''
                1
              /   \
             2     3
            / \     \
           4   5     7

'''