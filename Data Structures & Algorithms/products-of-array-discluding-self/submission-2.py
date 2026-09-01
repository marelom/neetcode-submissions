class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        My_list = []
        product = 1
        for v in nums:
            My_list.append(product)
            product *= v

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            My_list[i] *= product
            product *= nums[i]

        return My_list    
    
