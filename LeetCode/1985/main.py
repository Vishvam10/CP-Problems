"""
DIFFICULTY : easy
TAGS : array, string, divide and conquer, sorting, heap (priority queue), quickselect
"""


class Solution:
    def kthLargestNumber(self, arr: List[str], k: int) -> str:
        arr.sort(key=lambda x: int(x), reverse=True)
        if k == len(arr):
            return str(arr[-1])
        return str(arr[k - 1])
