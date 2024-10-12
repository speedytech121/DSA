class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def pop(self):
        if self.head is None:
            return -1
        if self.head.next is None:
            return self.head
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        data = temp.next.data
        temp.next = None
        return data


obj = MyQueue()
obj.push(1)
obj.push(6)
obj.push(3)
obj.push(2)
obj.push(5)
obj.push(3)
print(obj.pop(), end=" ")
print(obj.pop(), end=" ")
print(obj.pop())
