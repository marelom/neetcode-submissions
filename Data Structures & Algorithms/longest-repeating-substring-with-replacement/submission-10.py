class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        arr = [0] * 26
        max_length = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            arr[index] += 1
        
        # Trova la frequenza massima attuale nella finestra
            max_freq = 0
            for v in range(26):
                if arr[v] > max_freq:
                    max_freq = arr[v]
        
            window = right - left + 1

        # Se la finestra non è valida, stringi da sinistra
            if (window - max_freq) > k:
                left_index = ord(s[left]) - ord('A')
                arr[left_index] -= 1  # CORRETTO: togliamo il carattere di sinistra
                left += 1

            max_length = max(max_length, right - left + 1)            

        return max_length
