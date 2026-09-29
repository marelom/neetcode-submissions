class MinStack:

    def __init__(self):
        self.stack = []
        self.minsstack = []


    def push(self, val: int) -> None:
        if not self.stack:
            self.minsstack.append(val)
            self.stack.append(val)
            return
        el = min(val, self.minsstack[-1])
        self.minsstack.append(el)
        self.stack.append(val)    

            



    def pop(self) -> None:
        self.stack.pop()
        self.minsstack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minsstack:
            return None
        return  self.minsstack[-1]
