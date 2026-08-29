class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        My_Dict = {}
        strs_ord = [''.join(sorted(s)) for s in strs]

        for s in strs:
            key = ''.join(sorted(s))
            if key in My_Dict:
                My_Dict[key].append(s)
            else:
                My_Dict[key] = [s]    



        return list(My_Dict.values())         