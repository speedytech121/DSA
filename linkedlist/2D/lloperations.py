class Node:
    def __init__(self,prev=None, data=None, next=None):
        self.prev=prev
        self.data=data
        self.next=next
class DLinkedlist:
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        return self.head==None

    def insert_at_start(self,data):
        newnode=Node(None,data,self.head)
        if not self.is_empty():
            self.head.prev=newnode
        self.head=newnode
    
    def insert_at_end(self,data):
        newnode=Node(None,data,None)

        if self.is_empty():
            self.head=newnode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newnode
            newnode.prev=temp

    
    def printll(self):
        if self.head is None:
            print("The list is empty")
            return
        
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

obj=DLinkedlist()
obj.insert_at_end(1)
obj.insert_at_end(2)
obj.insert_at_end(3)
obj.printll()