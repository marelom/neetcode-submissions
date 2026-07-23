class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        le_set = set()
        for v in nums:
            if v in le_set:
                return True       
            le_set.add(v)

        return False
 


                
         