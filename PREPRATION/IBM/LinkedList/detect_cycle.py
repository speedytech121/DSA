# detect cycle in linkedlist
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

    def detectcycle(self):
        if not self.head or not self.head.next:
            return "no head->not detected"  # Empty or single-node list can't have a cycle

        slowp = self.head
        fastp = self.head
        while fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
            if slowp == fastp:
                return "detected"
        return "not detected"

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


obj = LinkedList()
obj.add_at_last(node1)
obj.add_at_last(node2)
obj.add_at_last(node3)
obj.add_at_last(node4)
obj.add_at_last(node5)


node5.next = node3 #cycle detected
print(obj.detectcycle())