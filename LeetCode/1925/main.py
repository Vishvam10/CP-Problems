"""
DIFFICULTY : easy
TAGS : math, enumeration
"""


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                sq = a * a + b * b
                c = int(sq**0.5)
                if c * c == sq and c <= n:
                    count += 2
        return count
