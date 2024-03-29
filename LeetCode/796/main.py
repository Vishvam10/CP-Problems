"""
DIFFICULTY : easy
TAGS : string, string matching
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        def rotate(s):
            n = len(s)
            temp = s[0]
            return s[1:n+1] + temp

        n = len(s)
        while (n > 0):
            if (rotate(s) == goal):
                return True
            s = rotate(s)
            n -= 1

        return False
