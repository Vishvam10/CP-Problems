"""
DIFFICULTY : medium
TAGS : array, greedy, sorting
"""


class Solution:
    def findMinArrowShots(self, pts: List[List[int]]) -> int:
        pts.sort(key=lambda x: x[1])
        cur = pts[0][1]
        count = 1
        for (st, end) in pts:
            if (st > cur):
                cur = end
                count += 1

        return count
