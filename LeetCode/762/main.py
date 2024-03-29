"""
DIFFICULTY : easy
TAGS : array, bit manipulation
"""
import math


class Solution:
    def isPrime(self, n):
        if (n <= 1):
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if (n % i == 0):
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            if (self.isPrime(bin(i).count("1"))):
                count += 1
        return count
