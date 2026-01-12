class Solution:
    def trap(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        # Max greatest element to the left for each element (prefix array)
        lefts = [0] * n
        lefts[0] = arr[0]

        # Max greatest element to the right for each element (suffix array)
        rights = [0] * n
        rights[n - 1] = arr[n - 1]

        for i in range(1, n, 1):
            lefts[i] = max(lefts[i - 1], arr[i])

        for i in range(n - 2, -1, -1):
            rights[i] = max(rights[i + 1], arr[i])

        for i in range(n):
            height = min(lefts[i], rights[i]) - arr[i]
            ans += height

        return ans
