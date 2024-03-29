"""
DIFFICULTY : easy
TAGS : math, string
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = []
        while n:
            n, r = divmod(n - 1, 26)
            ans.append(chr(r + ord("A")))
        return "".join(reversed(ans))
