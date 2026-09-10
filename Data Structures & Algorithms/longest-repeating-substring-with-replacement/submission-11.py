class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = 0
        left = 0
        arr = [0] * 26
        freq = 0
        max_length = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            arr[index] += 1
            
            max_freq = 0
            for v in range(26):
                if arr[v] > max_freq:
                    max_freq = arr[v]
            window = right - left + 1

            if (window - max_freq) > k:
                left_index = ord(s[left]) - ord('A')
                arr[left_index] -= 1
                left += 1

            window = right - left + 1
            max_length = max(max_length, window)            


        return max_length            


