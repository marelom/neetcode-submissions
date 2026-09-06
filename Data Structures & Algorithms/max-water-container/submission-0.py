class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0
        left_biggest = 0
        right_biggest = 0
        biggest_width = 0
        biggest_length = 0
        biggest_most = 0
        left_idx = 0
        right_idx = 0
        while left < right:
            width = right - left
            length = min(heights[left], heights[right])
            most = width * length
            if heights[left] < heights[right]:
                if most >= biggest_most:
                    biggest_most = most
                left += 1
            else:
                if most >= biggest_most:
                    biggest_most = most
                right -= 1  

        return (biggest_most)              
    