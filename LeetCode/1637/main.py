"""
DIFFICULTY : medium
TAGS : array, sorting
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_diff = 0
        points = sorted(points, key=lambda x: x[0])
        for i in range(1, len(points)):
            xc1 = points[i][0]
            xc2 = points[i-1][0]
            max_diff = max(max_diff, abs(xc1 - xc2))
        return max_diff
