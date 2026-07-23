class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_remove = [" ", ",", ".", "?", "'", "!", ":", ";", "*", "&"]
        clean_s = s.lower()
        for character in to_remove:
            clean_s = clean_s.replace(character, "")
        reversed_s = clean_s[::-1]
        if reversed_s == clean_s:
            return True
        else:
            return False    