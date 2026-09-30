class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0] * n
        for v in range(n - 2, -1, -1):
            curr = temperatures[v]
            j = v + 1
            while j < n:
                if temperatures[j] > curr:
                    stack[v] = j - v
                    break
                elif stack[j] == 0:
                    break
                else:
                    j += stack[j]        



        return stack        
            