"""
DIFFICULTY : easy
TAGS : math, string, greedy
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        left = 0
        right = n - 1
        while (right >= 0):
            if (int(num[right]) % 2 == 0):
                right -= 1
            else:
                break
        if (right < 0):
            return ""
        return num[:right+1]
