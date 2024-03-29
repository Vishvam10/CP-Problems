"""
DIFFICULTY : easy
TAGS : array, two pointers, string
"""


class Solution:
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while (i < j):
            if (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for i in range(len(words)):
            if (self.isPalindrome(words[i])):
                return words[i]
        return ""
