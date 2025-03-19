'''Doubly Linked List operations:
isempty, isertatstart, insertatend, search, insertafter,
deletefirst, deletelast, deleteitem, printll '''

class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev=prev
        self.data=data
        self.next=next

class DLinkedList:
    def __init__(self):
        self.head=None

    def isempty(self):
        return self.head==None

    def insertatstart(self,data):
        newnode=Node(None,data,self.head)
        if not self.isempty():
            self.head.prev=newnode
        self.head=newnode

    def insertatend(self,data):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        newnode=Node(temp,data,None)
        temp.next=newnode
    
    def insertafter(self, item, data):
        temp=self.head 
        while temp is not None:
            if temp.data==item:
                newnode=Node(temp,data,temp.next)
                if temp.next is not None:
                    temp.next.prev=newnode
                temp.next=newnode
            temp=temp.next


    def search(self, data):
        temp=self.head
        count=0
        while temp is not None:
            if temp.data==data:
                print(f"data found at: {count}")
            temp=temp.next
            count+=1


    def deletestart(self):
        temp=self.head
        if not self.isempty():
            self.head=temp.next
            temp.next.prev=None

    def deleteend(self):
        temp=self.head
        if not self.isempty():
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
            temp.prev=None


    def delete_item(self,data):
        temp=self.head
        if not self.isempty():
            while temp is not None:
                if temp.data==data:
                    if temp.prev==None:
                        self.deletestart()
                        return
                    if temp.next==None:
                        self.deleteend()
                        return

                    if temp.next is not None:
                        temp.prev.next=temp.next
                        temp.next.prev=temp.prev
                        return 
                    
                temp=temp.next

    def printll(self, *args):
        print(args[0])
        temp=self.head
        while temp:
            print(temp.data, end=',')
            temp=temp.next
        print('\n')

    def reversell(self):
        stack=[]
        temp=self.head
        while temp is not None:
            stack.append(temp.data)
            temp=temp.next
        for i in range(len(stack)):
            rdata=stack.pop(0)
            self.insertatstart(rdata)
            
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None



obj=DLinkedList()
obj.insertatstart(3)
obj.insertatstart(2)
obj.insertatstart(1)
obj.printll("print LL after insert start")
obj.insertatend(4)
obj.insertatend(5)
obj.insertatend(6)
obj.printll("print LL after insert at end")
obj.insertafter(1,22)
obj.insertafter(6,66)
obj.printll("insertafter")
obj.search(1)
obj.search(66)
obj.search(4)
obj.deletestart()
obj.printll("after delete start")
obj.deleteend()
obj.printll("after delete end")
obj.delete_item(22)
obj.delete_item(6)
obj.delete_item(3)
obj.printll("after delete item")
obj.printll("ll before reverse")
obj.reversell()
obj.printll("ll after reverse")

# need to check better optimized approach from takeyouforward.org