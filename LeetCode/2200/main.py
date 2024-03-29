class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = start ^ goal
        ans = 0

        while (res):
            lsb = res & 1
            if (lsb == 1):
                ans += 1
            res >>= 1

        return ans
