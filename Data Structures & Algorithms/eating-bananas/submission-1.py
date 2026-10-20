class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_b = 1
        max_b = max(piles)
        result = 0
        while min_b < max_b:
            mid = (min_b + max_b) // 2

            result = sum(math.ceil(pile / mid) for pile in piles)

            if result <= h:
                max_b = mid
            else:
                min_b = mid + 1    
        
        return min_b
