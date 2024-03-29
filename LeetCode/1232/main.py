"""
DIFFICULTY : easy
TAGS : array, math, geometry
"""


class Solution:
    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = arr[:2]
        for i in range(2, len(arr)):
            (x, y) = arr[i]
            if ((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True
