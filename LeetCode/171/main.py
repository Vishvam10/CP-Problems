"""
DIFFICULTY : easy
TAGS : math, string
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for ch in s:
            ans = (ord(ch) - 64) + 26 * ans
        return ans
