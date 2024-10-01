# if lenght is even the second middle else middle

# brute force

class Node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertdata(self,data):
        newnode=Node(data,None)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            self.head=newnode
            newnode.next=temp
    
    def reversell(self):
        prev=None
        curr=self.head
        while curr is not None:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        self.head=prev
    
    def findlength(self):
        temp=self.head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count
    def printll(self):
        temp=self.head
        if temp is not None:
            while temp is not None:
                print(temp.data, end='-')
                temp=temp.next
        else:
            print("ll is empty")

obj=LinkedList()
obj.insertdata(8)
obj.insertdata(7)
obj.insertdata(6)
obj.insertdata(5)
obj.insertdata(4)
obj.insertdata(3)
obj.insertdata(2)
obj.insertdata(1)

obj.printll()
print("\n")
obj.reversell()
obj.printll()