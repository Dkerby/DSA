class MinStack:
    def __init__(self):
        self.stack = []
        self.currentMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.currentMin) > 0:
            self.currentMin.append(min(val, self.currentMin[-1]))
        else:
            self.currentMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.currentMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin[-1]
