class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr_1 = [0] * 26
        arr_2 = [0] * 26

        if len(s1) > len(s2):
            return False
        

        for i in range(len(s1)):
            arr_1[ord(s1[i]) - ord('a')] += 1
            arr_2[ord(s2[i]) - ord('a')] += 1

        if arr_1 == arr_2:
            return True    

        for i in range(len(s1), len(s2)):
            right_index = ord(s2[i]) - ord('a')
            arr_2[right_index] += 1

            left_index = ord(s2[i - len(s1)]) - ord('a')
            arr_2[left_index] -= 1
            if arr_1 == arr_2:
                return True    
        return False        
            

     
            


        