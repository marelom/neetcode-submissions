class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0
        val = 0
        My_list = []
        record_val = 0
        for p, v in enumerate(s):
            if v not in My_list:
                My_list.append(v)
            else:
                idx = My_list.index(v)
                My_list = My_list[idx + 1:]
                My_list.append(v)

            if len(My_list) > record_val:
                record_val = len(My_list)
        return record_val        

           