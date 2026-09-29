class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if tokens is None:
            return 0
        for v in tokens:
            if v == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)
            elif v == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b * a)
            elif v == "-":
                a = int(stack.pop())
                b = int(stack.pop()) 
                stack.append(b - a)
            elif v == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b/a)
            else:
                stack.append(v)
            
        return int(stack[0])         

                