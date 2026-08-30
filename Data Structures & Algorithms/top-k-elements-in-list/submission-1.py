class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        My_dict = {}
        for v in nums:
            key = v

            if key in My_dict:
                My_dict[key] += 1
            else:
                My_dict[key] = 1

        My_list = []

        for n, f in My_dict.items():
            My_list.append((f, n)) 

        heapq.heapify(My_list)

        while len(My_list) > k:
            heapq.heappop(My_list)

        return [tupla[1] for tupla in My_list]

              