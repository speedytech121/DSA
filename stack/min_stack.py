class MinStack:
    def __init__(self):
        self.stack=[]

    def push(self, val):
        mini = self.get_minimum()
        if mini is not None and mini>val:
            mini=val
        self.stack.append(val)
        
    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_minimum(self):
        return min(self.stack) if self.stack else None

obj=MinStack()
obj.push(3)
obj.push(4)
obj.push(2)
obj.push(3)
print(f"At top is: {obj.top()}")
print(f"minimum is: {obj.get_minimum()} ")
print(f"stack is : {obj.stack}")