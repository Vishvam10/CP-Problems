"""
DIFFICULTY : easy
TAGS : math, recursion
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 0) or (x == 1):
            return 1

        if x == 0:
            return 0

        if n < 0:
            return self.myPow(1 / x, abs(n))

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)
