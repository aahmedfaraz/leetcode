class MyStack:

    def __init__(self):
        self.vals = []
        self.length = 0
        

    def push(self, x: int) -> None:
        self.vals.append(x)
        self.length += 1
        

    def pop(self) -> int:
        self.length -= 1
        return self.vals.pop()
        

    def top(self) -> int:
        return self.vals[self.length - 1]
        

    def empty(self) -> bool:
        return self.length == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()