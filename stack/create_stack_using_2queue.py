class MyStack:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    
    def push(self, x):
        self.q1.append(x)

    def pop(self):
        for i in range(len(self.q1)-1):
            self.q2.append(self.q1.pop(0))
        popped=self.q1.pop(0)
        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop(0))
        return popped

    def top(self):
        return self.q1[-1]

    def empty(self):
        return len(self.q1)==0

obj=MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.empty())
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.empty())