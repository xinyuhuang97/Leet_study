import math
class MinStack:

    def __init__(self):
        self.stack=[]
        self.stack_desc=[]
        self.lg=0
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_desc==[]:
            self.stack_desc.append(val)
        else:
            self.stack_desc.append(min(val, self.stack_desc[-1]))
        self.lg+=1

    def pop(self) -> None:
        self.stack.pop()
        self.stack_desc.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_desc[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()