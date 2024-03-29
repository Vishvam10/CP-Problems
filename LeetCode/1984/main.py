"""
DIFFICULTY : easy
TAGS : array, sliding window, sorting
"""


class Solution:
    def minimumDifference(self, arr: List[int], k: int) -> int:
        arr.sort()
        n = len(arr)

        min_diff = inf
        i = 0
        while (i+k <= n):
            min_diff = min(min_diff, arr[i+k-1] - arr[i])
            i += 1

        return min_diff
