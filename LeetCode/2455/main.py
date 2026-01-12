"""
DIFFICULTY : easy
TAGS : array, math
"""


class Solution:
    def averageValue(self, arr: List[int]) -> int:
        s = 0
        count = 0
        for x in arr:
            if x % 2 == 0 and x % 3 == 0:
                s += x
                count += 1
        if count == 0:
            return 0
        return s // count
