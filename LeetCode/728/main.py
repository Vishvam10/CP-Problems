"""
DIFFICULTY : easy
TAGS : math
"""


class Solution:
    def check(self, num):
        x = num
        while num > 0:
            digit = num % 10
            num = num // 10
            if digit == 0:
                return False
            if x % digit != 0:
                return False
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if self.check(i):
                ans.append(i)
        return ans
