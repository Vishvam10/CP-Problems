from collections import defaultdict


class Solution:
    def characterReplacement(self, arr: str, k: int) -> int:
        n = len(arr)
        mp = defaultdict(int)
        left, maxi, ans = 0, 0, 0

        for i in range(n):
            mp[arr[i]] += 1
            maxi = max(maxi, mp[arr[i]])
            ws = i - left + 1

            if ws - maxi > k:
                mp[arr[left]] -= 1
                left += 1

            else:
                ans = max(ans, i - left + 1)

        return ans
