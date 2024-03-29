"""
DIFFICULTY : easy
TAGS : math, recursion
"""


class Solution:
    # Maximum power of 3 (in int) : 3^(log_3(INT_MAX))
    # INT_MAX = 2^31 / 2 - 1 (half of them is negative
    # and exclude 0)

    # So, max power of 3 (in int) is 3^19 = 1162261467
    # Since 3 is a prime number, the only divisors of 3^19
    # are 3^0, 3^1 ... 3^19, therefore all we need to do is
    # divide 3^19 by n. A remainder of 0 means n is a divisor
    # of 319319 and therefore a power of three.
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (1162261467 % n == 0)
