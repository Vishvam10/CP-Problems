"""
DIFFICULTY : medium
TAGS : array, math, divide and conquer, geometry, heap, quickselect, sorting
"""
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, lambda (x, y): x*x + y*y)
