class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def checkpalindrome(head):
    li1,li2=[],[]
    temp=head
    while temp.next is not None:
        li1.append(temp.data)
        temp=temp.next
    
    newnode=reverse_linked_list(head)
    while newnode.next is not None:
        li2.append(newnode.data)
        newnode=newnode.next
    if li1==li2:
        return True
    else:
        return False


def reverse_linked_list(head):
    if not head:
        return None
    newhead=head
    if head.next:
        newhead=reverse_linked_list(head.next)
        head.next.next=head
    head.next=None
    return newhead


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)

print(checkpalindrome(head))




