"""
DIFFICULTY : easy
TAGS : math
"""
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        return 0 if rev > pow(2, 31) else rev * flag