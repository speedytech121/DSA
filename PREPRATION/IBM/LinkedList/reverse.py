# reverse a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_last(self, newnode):
        if self.head is None:
            self.head = newnode
        elif self.head:
            temp_head = self.head
            while temp_head.next:
                temp_head = temp_head.next
            temp_head.next = newnode
            
    def add_at_start(self,newnode):
        if self.head is None:
            self.head = newnode
            return
        temp_head = self.head
        self.head = newnode
        newnode.next = temp_head

    def printlist(self):
        temp_head = self.head
        while temp_head:
            print(temp_head.data, end=" -> ")
            temp_head = temp_head.next
        print("None")
            
    def reverselist(self):
        prev = None
        curr = self.head
        while curr is not None:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        self.head = prev

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

obj = LinkedList()
# obj.add_at_start(node1)
# obj.add_at_start(node2)
# obj.add_at_start(node3)
# obj.add_at_start(node4)

obj.add_at_last(node1)
obj.add_at_last(node2)
obj.add_at_last(node3)
obj.add_at_last(node4)

obj.printlist()
obj.reverselist()
obj.printlist()