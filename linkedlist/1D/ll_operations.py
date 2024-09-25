class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def add_start(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node

    def findlength(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        print(f'length of ll is: {count}')

    def searchelement(self,target):
        current=self.head
        while current:
            if current.data==target:
                print(target)
                return
            current=current.next

    def print_ll(self):
        current=self.head
        while current:
            print(current.data, end='->')
            current=current.next
        print("None")

ll=LinkedList()
ll.add_start(3)
ll.add_start(2)
ll.add_start(1)

ll.add_end(4)
ll.add_end(5)
ll.add_end(6)

ll.print_ll()
ll.findlength()
ll.searchelement(5)