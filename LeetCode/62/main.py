"""
DIFFICULTY : medium
TAGS : math, dp, combinatorics
"""

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tot = m + n - 2
        num = math.factorial(tot)
        den = math.factorial(m - 1) * math.factorial(n - 1)
        return num // den
