class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        if self.min == None or x < self.min: 
            self.min = x
        self.stack.append(x)

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
        else:
            self.min = min(self.stack)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()