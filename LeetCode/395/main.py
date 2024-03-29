from collections import defaultdict


class Solution:
    def longestSubstring(self, arr: str, k: int) -> int:

        n = len(arr)
        mp = defaultdict(int)

        for x in arr:
            mp[x] += 1

        left, ans = 0, 0

        for i in range(n):
            if (mp[arr[i]] < k):
                left = i
            else:
                ans = max(ans, i - left + 1)

        return ans
