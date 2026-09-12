class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_par = {')': '(', ']': '[', '}': '{'}
        for v in s:
            if v in map_par:
                element = stack.pop() if stack else '#'
                if map_par[v] != element:
                    return False
            else:
                stack.append(v) 

        if len(stack) == 0:
            return True
        else:
            return False              

                


