class MinStack:

    def __init__(self):
        self.stack = []
        self.getMinNum = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.getMinNum) == 0 or val < self.getMinNum[-1]:
            self.getMinNum.append(val)
        else:
            self.getMinNum.append(self.getMinNum[-1])
            

    def pop(self) -> None:
        self.getMinNum.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.getMinNum[-1]