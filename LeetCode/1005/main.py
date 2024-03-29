"""
DIFFICULTY : easy
TAGS : array, greedy, sorting
"""


class Solution:
    def largestSumAfterKNegations(self, arr: List[int], k: int) -> int:
        arr.sort()
        i = 0
        while (i < len(arr) and i < k and arr[i] < 0):
            arr[i] = -arr[i]
            i += 1
        return sum(arr) - (k - i) % 2 * min(arr) * 2
