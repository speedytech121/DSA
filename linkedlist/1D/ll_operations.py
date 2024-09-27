class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# insert at start, end, search, print, delete, update, insert at index
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insertatstart(self, data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def insertatend(self,data):
        newnode=Node(data)
        current=self.head
        while current.next!=None:
            current=current.next
        current.next=newnode

    def insertatindex(self,data, index):
        newnode=Node(data)
        if self.head is None:
            print("list is empty")
            return
        if index==0:
            newnode.next=self.head
            self.head=newnode
            return
        
        current=self.head
        previous=None
        count=0
        while count<index:
            previous=current
            current=current.next
            count+=1
        
        previous.next=newnode
        newnode.next=current


        
    def deleteatindex(self, index):
        if self.head is None:
            print("list is empty")
            return
        
        if index==0:
            self.head=self.head.next
            return
        
        current=self.head
        previous=None
        count=0

        while current and count<index:
            previous = current
            current = current.next
            count+=1

        if current is None:
            print("index out of range")
            return
        previous.next=current.next


    def updateatindex(self,data, index):
        self.deleteatindex(index)
        self.insertatindex(data,index)
        
    
    def searchelement(self,data):
        current=self.head
        index=0
        while current:
            if current.data==data:
                return index
            current=current.next
            index+=1 

    def printll(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

obj=Linkedlist()
obj.insertatstart(4)
obj.insertatstart(3)
obj.insertatstart(2)
obj.insertatstart(1)

print("LL after inserting at start-")
obj.printll()

obj.insertatend(5)
obj.insertatend(6)

print("LL after inserting at end-")
obj.printll()

obj.deleteatindex(2)
print("ll after deletion at index")
obj.printll()


obj.insertatindex(3,2)
obj.insertatindex(31,3)
obj.insertatindex(32,4)
print("insert at index")
obj.printll()


obj.updateatindex(30,2)
print("update at index")
obj.printll()


print("searching an element")
print(obj.searchelement(30))
print(obj.searchelement(32))