"""
DIFFICULTY : medium
TAGS : array, dp, greedy
"""


class Solution:
    # DP : The FARTHEST INDEX we can reach given
    #      allowed steps from 0 to i
    # Greedy : A bit similar to Kadane's Algorithm
    def canJump(self, arr: List[int]) -> bool:
        n = len(arr)
        ans = [0] * n

        ans[0] = arr[0]

        for i in range(1, n - 1):
            if ans[i - 1] < i:
                return False

            ans[i] = max(i + arr[i], ans[i - 1])

            if ans[i] >= n - 1:
                return True

        return ans[n - 2] >= n - 1
