"""
DIFFICULTY : medium
TAGS : math, enumeration
"""


class Solution:
    def sumOfNumberAndReverse(self, n: int) -> bool:
        def rev(n):
            ans = 0
            while n:
                ans = (ans * 10) + n % 10
                n //= 10
            return ans

        for i in range(n // 2, n + 1):
            if i + rev(i) == n:
                return True
        return False
