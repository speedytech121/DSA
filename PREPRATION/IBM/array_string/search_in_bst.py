# check value is present in the binary search tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search_bst(root, key):
    if root is None:
        return False
    
    if root.val == key:
        return True
    elif key<root.val:
        return search_bst(root.left, key)
    else:
        return search_bst(root.right, key)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print(search_bst(root, 7))
print(search_bst(root, 8))