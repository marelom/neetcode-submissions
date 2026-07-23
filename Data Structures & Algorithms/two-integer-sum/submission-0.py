class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        le_dict = {}
        for p, v in enumerate(nums):
            partner = target - v
            if partner in le_dict:
                return [le_dict[partner], p]
            le_dict[v] = p    