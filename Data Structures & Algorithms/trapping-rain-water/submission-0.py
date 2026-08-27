class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        right = len(height) - 1
        left = 0
        new_left_highest = 0
        new_right_highest = 0

        while left < right:
            if height[left] < height[right]:
    
                if height[left] >= new_left_highest:
                    new_left_highest = height[left]  
                else:
                    water += new_left_highest - height[left]
                left += 1
            else: 
                if height[right] >= new_right_highest:
                        new_right_highest = height[right]  
                else:
                    water += new_right_highest - height[right]    
                right -= 1



        return water     