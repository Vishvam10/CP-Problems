"""
DIFFICULTY : easy
TAGS : math, bit manipulation, recursion
"""


class Solution:
    # (n - 1) % 3 makes sures that the 1 occurs in odd
    # places. For example, in 16 : 00010000.

    # To make is more efficient, we can use the bit mask :
    # 1010101010101010101010101010101 and AND it with n

    # That number is 1431655765 in decimal and 55555555
    # in hex
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
