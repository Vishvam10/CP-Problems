"""
DIFFICULTY : easy
TAGS : math, greedy
"""


class Solution:
    def maximum69Number(self, n: int) -> int:
        m = n
        ind = -1
        curr = 0
        while m:
            if m % 6 == 0:
                ind = curr
            m //= 10
            curr += 1

        if ind == -1:
            return n
        else:
            return n + 3 * (10**ind)
