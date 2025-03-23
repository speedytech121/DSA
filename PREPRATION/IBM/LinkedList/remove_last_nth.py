# Remove the nth node from the end of a linked list.​
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertatlast(self, newnode):
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def llLength(self):
        temp = self.head
        length = 0
        while temp:
            length+=1
            temp = temp.next
        return length

    def removeLastNthNode(self, n):
        idx = self.llLength() - n
        print(f"\nexact index is {idx}")
        if idx == 0:
            return None
        temp = self.head
        prev = None
        for i in range(idx):
            prev = temp
            temp = temp.next
        nextNode = temp.next
        temp.next = None
        prev.next = nextNode
            
            
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

obj = LinkedList()
obj.insertatlast(node1)
obj.insertatlast(node2)
obj.insertatlast(node3)
obj.insertatlast(node4)
obj.insertatlast(node5)

obj.printList()
obj.removeLastNthNode(2)
obj.printList()

