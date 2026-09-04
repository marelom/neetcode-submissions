class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None:
            return None
        left = 0
        right = len(numbers) - 1

        while left < right:
            start = numbers[left]
            search = numbers[right]
            sol = target - start
            if search == sol:
                return list((left + 1, right + 1))
            elif search < sol:
                left += 1
            else:
                right -= 1   
