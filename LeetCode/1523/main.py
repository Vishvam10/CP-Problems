class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high - low + 1

        if (low % 2 != 0 and high % 2 != 0):
            return n//2 + 1
        else:
            return n//2
