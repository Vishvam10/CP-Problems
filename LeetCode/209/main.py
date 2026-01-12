"""
DIFFICULTY : medium
TAGS : array, binary search, sliding window, prefix sum
"""


class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        ans = float("inf")
        s = 0
        for i in range(n):
            s += arr[i]
            while s >= target:
                ans = min(ans, i - left + 1)
                s -= arr[left]
                left += 1

        if ans == float("inf"):
            return 0
        return ans
