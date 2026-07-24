class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for p, v in enumerate(nums):
            if v == target:
                return p
        return -1        