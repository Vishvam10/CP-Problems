"""
DIFFICULTY : medium
TAGS : math, string, simulation
"""


class Solution:
    def convertToInt(self, num: str) -> int:
        power = 1
        ans = 0
        for digit in reversed(num):
            ans += power * (ord(digit) - ord('0'))
            power *= 10
        return ans

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convertToInt(num1) * self.convertToInt(num2))
