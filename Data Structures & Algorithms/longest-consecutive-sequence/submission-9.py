class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        
        My_set = set(nums)
        sorted_nums = sorted(My_set)
        new_nums = list(sorted_nums)
        number = 1
        new_streak = 0
        key_next = 0
        
        for i, v in enumerate(new_nums):
            if i != len(new_nums) - 1:
                key_next = new_nums[i + 1]
                
            if key_next == v + 1:
                number += 1
            else:
                new_streak = max(new_streak, number)
                number = 1    

        return new_streak        


                
      
