class MinStack:

    def __init__(self):
        self.stack = []
        # self.mini = float('inf')
        self.minStack = [float('inf')]

    def push(self, val: int) -> None:
        if val <= self.minStack[len(self.minStack)-1]:
            self.minStack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[len(self.stack)-1] == self.minStack[len(self.minStack)-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1] if len(self.minStack) > 0 else "null"
        # null should not with "" but it gives me an error without it


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
