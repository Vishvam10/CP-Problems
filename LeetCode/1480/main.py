"""
DIFFICULTY : easy
TAGS : array, prefix sum
"""


class Solution:
    def runningSum(self, arr: List[int]) -> List[int]:
        pre = [None] * len(arr)
        pre[0] = arr[0]
        for i in range(1, len(arr)):
            pre[i] = pre[i - 1] + arr[i]
        return pre
