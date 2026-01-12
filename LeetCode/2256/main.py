"""
DIFFICULTY : medium
TAGS : array, prefix sum
"""


class Solution:
    def minimumAverageDifference(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * n
        pre[0] = arr[0]
        min_diff = inf
        min_ind = 0

        for i in range(1, n):
            pre[i] = pre[i - 1] + arr[i]

        # suffix sum is simply pref[n - 1] - pref[i]

        for i in range(n):
            diff = abs(
                (pre[i] // (i + 1)) - ((pre[n - 1] - pre[i]) // max(n - i - 1, 1))
            )
            if diff < min_diff:
                min_diff = diff
                min_ind = i

        return min_ind
