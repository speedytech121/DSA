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

    def remvoeelements(self,data):
        if(self.head==None):
            return None
        while(self.head!=None and self.head.data==data): #eliminate starting mathced element
            self.head=self.head.next

        current=self.head
        while(current!=None and current.next!=None):
            if(current.next.data==data):
                current.next=current.next.next
            else:
                current=current.next


    def printll(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next

obj=Linkedlist()

obj.insertatstart(6)
obj.insertatstart(5)
obj.insertatstart(4)
obj.insertatstart(3)
obj.insertatstart(6)
obj.insertatstart(2)
obj.insertatstart(1)

# obj.insertatstart(7)
# obj.insertatstart(7)
# obj.insertatstart(7)
# obj.insertatstart(7)

obj.printll()

print("after remove element")
# obj.remvoeelements(7)
obj.remvoeelements(6)
obj.printll()