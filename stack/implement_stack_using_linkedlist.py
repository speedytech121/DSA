class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class MyStack:
    def __init__(self):
        self.head=None

    def push(self, data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def pop(self):
        if not self.head:
            return -1
        else:
            data=self.head.data
            self.head=self.head.next
        return data

obj=MyStack()
obj.push(2)
obj.push(5)
obj.push(4)
obj.push(3)
obj.push(1)
print(obj.pop())
print(obj.pop())
print(obj.pop())
