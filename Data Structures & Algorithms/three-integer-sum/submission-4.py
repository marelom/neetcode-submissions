class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)  
        My_list = []
        
        for i in range(len(sort_nums) - 2):

            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue

            left = i + 1
            right = len(sort_nums) - 1  

            while left < right:
                start = sort_nums[left]
                search = sort_nums[right]
                target = -sort_nums[i]
                
                if start + search == target:
                    My_list.append([sort_nums[i], start, search])
                    
                    while left < right and sort_nums[left] == sort_nums[left + 1]:
                        left += 1
                    while left < right and sort_nums[right] == sort_nums[right - 1]:
                        right -= 1    
                    
                    left += 1
                    right -= 1
                
                elif start + search < target:
                    left += 1
                else:
                    right -= 1
                
        return My_list
       

         
