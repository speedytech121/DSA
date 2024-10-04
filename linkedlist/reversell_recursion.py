class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse_linked_list(head):
    if not head:
        return None
    newhead=head
    if head.next:
        newhead=reverse_linked_list(head.next)
        head.next.next=head
    head.next=None
    return newhead


# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

print("Original Linked List:", end=" ")
print_linked_list(head)

head = reverse_linked_list(head)

print("Reversed Linked List:", end=" ")
print_linked_list(head)


