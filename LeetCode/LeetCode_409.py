class Solution:
    # Focus on string lengths not the characters    
    
    # NOTE : v & 1 is equivalent v % 2 == 1
    #        bool(integer) = 0, if integer = 0
    #                      = 1, otherwise (including integer < 0)
    
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)