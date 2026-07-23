class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for value  in nums:
            if value in my_set:
                return True

            my_set.add(value)
        

        return False
                
         