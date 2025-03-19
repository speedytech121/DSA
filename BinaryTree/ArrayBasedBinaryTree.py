'''
------------ Array Representation of a Binary Tree -----------------
Root Node is at index 0.
Left Child of Node at index i is at 2*i + 1.
Right Child of Node at index i is at 2*i + 2.
Parent of Node at index i is at (i-1) / 2.

ADVANTAGE:
1. memory efficient for complete trees(no extra pointer storage).
2. direct access using index calculations(O(1) access)
3. simple implementation

DISADVANTAGE:
1. Inefficient for sparse Trees - wastes space for missin nodes.
2. Insertion & Deletion is costly = resizing or shifting required
3. Not Ideal for Dynamic Trees - If the structure changes often, linked representation is better.


'''
class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size
    
    def set_root(self, value):
        self.tree[0] = value
    
    def set_left(self, parent_index, value):
        left_index = 2 * parent_index + 1
        if left_index < self.size:
            self.tree[left_index] = value
        else:
            print("left child index out of bounds!")
    
    def set_right(self, parent_index, value):
        right_index = 2 * parent_index + 2
        if right_index < self.size:
            self.tree[right_index] = value
        else:
            print("right child index out of bounds!")
    
    def get_parent(self, child_index):
        if child_index == 0:
            return None
        return self.tree[(child_index - 1) // 2]
    
    def display(self):
        print(f"Binary Tree as array: {self.tree}")

bt = BinaryTree(10)
bt.set_root("A")
bt.set_left(0, "B")
bt.set_right(0, "C")
bt.set_left(1, "D")
bt.set_right(1,"E")
bt.set_left(2,"F")
# bt.set_right(2, "G")
# bt.set_left(3,"H")
# bt.set_right(3, "I")
# bt.set_left(4, "k")


bt.display()