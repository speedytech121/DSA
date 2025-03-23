'''
Traverse the head1 and head2 until they are nullptr. Let head1 reaches to end first then set head1 to the
starting point of head2 and same for head2 . then in the next loop it is gurenteed that they will come at
the point of intersection. Dry run it and try.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def intersectPoint(self, head1, head2):
        temp1 = head1
        temp2 = head2
        
        while temp1 != temp2:
            temp1 = head2 if temp1 is None else temp1.next
            temp2 = head1 if temp2 is None else temp2.next
        
        return temp1  # Return the node itself, not just the data


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Creating two linked lists with an intersection
head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head1.next.next.next = Node(40)  # Intersection starts here
head1.next.next.next.next = Node(50)
head1.next.next.next.next.next = Node(60)

head2 = Node(5)
head2.next = Node(15)
head2.next.next = head1.next.next.next  # Intersecting at node 40

# Printing the lists
print("List 1:")
print_list(head1)

print("\nList 2:")
print_list(head2)

# Finding intersection
solution = Solution()
intersect_node = solution.intersectPoint(head1, head2)

# Printing result
if intersect_node:
    print(f"\nIntersection found at node with data: {intersect_node.data}")
else:
    print("\nNo intersection found")
