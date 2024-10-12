class MyQueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    
    def push(self,x):
        self.s1.append(x)

    def pop(self):
        for i in range(len(self.s1)-1):
            self.s2.append(self.s1.pop())
        popped=self.s1.pop()
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return popped

    def peek(self):
        return self.s1[0]

    def empty(self):
        return len(self.s1)==0