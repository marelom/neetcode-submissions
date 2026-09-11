class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr_1 = [0] * 26
        arr_2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for l in s1:
            index = ord(l) - ord('a')
            arr_1[index] += 1
        

        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            arr_2[index] += 1

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
            

     
            


        