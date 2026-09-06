class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        biggest_most = 0
        while left < right:
            width = right - left
            length = min(heights[left], heights[right])
            most = width * length

            if most >= biggest_most:
                biggest_most = most

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1  

        return (biggest_most)              
    