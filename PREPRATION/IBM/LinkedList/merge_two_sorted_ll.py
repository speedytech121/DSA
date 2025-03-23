# merge two sorted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertatlast(self, newnode):
        if not self.head:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        
    def insertatstart(self, newnode):        
        if not self.head:
            self.head = newnode
            return
        tempnode = self.head
        self.head = newnode
        newnode.next = tempnode
    
    def printnode(self):
        tempnode= self.head
        while tempnode.next:
            print(tempnode.data)
            tempnode = tempnode.next

def merge(ll1, ll2):
    curr = temp = Node(None)
    while ll1 and ll2:
        if ll1.data<ll2.data:
            curr.next = ll1
            ll1=ll1.next
        else:
            curr.next = ll2
            ll2 = ll2.next
        curr = curr.next
    curr.next = ll1 if ll1 else ll2
    return temp.next

node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(40)

ll1 = LinkedList()
ll1.insertatlast(node1)    
ll1.insertatlast(node2)    
ll1.insertatlast(node3)    
ll1.insertatlast(node4)

node1 = Node(2)
node2 = Node(3)
node3 = Node(20)
ll2 = LinkedList()
ll2.insertatlast(node1)
ll2.insertatlast(node2)
ll2.insertatlast(node3)


merged_head = merge(ll1.head, ll2.head)
print(f"merged linked list")
merged_list = LinkedList()
merged_list.head = merged_head
merged_list.printnode()


