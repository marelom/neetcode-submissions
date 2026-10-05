class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        height = 0
        area = 0
        heights.append(0)
        for i, v in enumerate(heights):
            height = v
            right = i + 1
            left = i - 1
            width = 1
            while stack and heights[stack[-1]] > height:
                obj = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1 

                result = heights[obj] * width
                if area < result:
                    area = result        
            stack.append(i)        
            
        return area