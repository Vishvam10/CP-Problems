"""
DIFFICULTY : easy
TAGS : math
"""


class Solution:
    def countDigits(self, n: int) -> int:
        ans = 0
        temp = n
        while (n > 0):
            digit = n % 10
            if (temp % digit == 0):
                ans += 1
            n //= 10
        return ans
