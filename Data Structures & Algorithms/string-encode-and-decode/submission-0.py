class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            piece = f"{len(s)}#{s}"
            result += piece

        return result
    def decode(self, s: str) -> List[str]:
        My_list = []
        i = 0
        j = 0
        while i < len(s):
            t = s[i]
            k = s[j]
            if k == "#":
                new_text = s[i:j]
                number = int(new_text)
                word = s[j + 1: j + 1 + number]
                My_list.append(word)
                i = j + 1 + number
                j = i
            j += 1
        return My_list 

            
