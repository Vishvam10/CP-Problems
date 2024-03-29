"""
DIFFICULTY : easy
TAGS : array, prefix sum
"""


class Solution:
    # Use prefix sum or better 2 pointers
    def findMiddleIndex(self, arr: List[int]) -> int:
        ls = 0
        rs = sum(arr)

        for i in range(len(arr)):
            if (ls == rs - arr[i]):
                return i
            ls += arr[i]
            rs -= arr[i]
        return -1
