class MinStack:
    # STRUCTURE OF STACK ELEMENT : (val, minSoFar)
    def __init__(self):
        self.stack = []
        
    def push(self, val):
        self.stack.append((val, min(self.getMin(), val))) 
           
    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return float("inf")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()