"""
DIFFICULTY : easy
TAGS : array, two pointers, greedy, string
"""


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low = 0
        high = n
        ans = [0] * (n + 1)
        for i in range(n):
            if s[i] == "D":
                ans[i] = high
                high -= 1
            else:
                ans[i] = low
                low += 1
        ans[n] = low
        return ans
