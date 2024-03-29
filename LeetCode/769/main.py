class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        maxi, ans = float('-inf'), 0
        for i in range(n):
            maxi = max(maxi, arr[i])
            if (maxi <= i):
                ans += 1
        return ans
