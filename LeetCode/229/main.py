from collections import defaultdict


class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if (n == 1):
            return arr

        mp = defaultdict(int)
        ans = []

        for x in arr:
            mp[x] += 1

        for k, v in mp.items():
            if (v > n//3):
                ans.append(k)

        # print(ans)

        return ans
