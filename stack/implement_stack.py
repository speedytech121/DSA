class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        if len(self.arr)==0:
            return -1
        popped = self.arr.pop()
        return popped

obj= Stack()
obj.push(1)
obj.push(3)
obj.push(4)
obj.push(5)
obj.pop()
print(obj.arr)