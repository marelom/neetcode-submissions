class Solution:
    import heapq
    from typing import List
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]

        if stones is None:
            return None

        heapq.heapify(stones)

        number = 0

        while len(stones) >= 2:
            value_1 = heapq.heappop(stones)
            value_2 = heapq.heappop(stones)
            if value_1 != value_2:
               new_number =  abs(value_1 - value_2)              
               heapq.heappush(stones, -new_number)    
        
  

        return abs(stones[0]) if len(stones) == 1 else 0
