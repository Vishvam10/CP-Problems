"""
DIFFICULTY : easy
TAGS : string, greedy
"""
class Solution:
    def minTimeToType(self, word: str) -> int:
        count = len(word)  # To write the character, we take 1 second
        prev = "a"
        for ch in word :
            diff = (ord(ch) - ord(prev)) % 26
            count += min(diff, 26 - diff)
            prev = ch

        return count