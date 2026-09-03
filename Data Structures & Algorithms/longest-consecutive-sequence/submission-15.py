class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Creiamo il set (la ricerca dentro un set in Python è istantanea, richiede tempo O(1))
        my_set = set(nums)
        longest_streak = 0

        for v in my_set:
            # TRUCCO SEGRETO: Controlliamo se 'v' è il numero di INIZIO di una sequenza
            # Se esiste v - 1, significa che v NON è l'inizio, quindi lo saltiamo!
            if (v - 1) not in my_set:
                current_num = v
                current_streak = 1

                # Finché nel set c'è il numero successivo, allunghiamo la striscia
                while (current_num + 1) in my_set:
                    current_num += 1
                    current_streak += 1

                # Salviamo la striscia più lunga trovata finora
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


                
      
