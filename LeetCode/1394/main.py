"""
DIFFICULTY : easy
TAGS : array, counting, hash table
"""


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = {}
        ans = -1
        for x in arr:
            if (x not in mp):
                mp[x] = 1
            else:
                mp[x] += 1
        for k, v in mp.items():
            if (k == v):
                ans = max(ans, v)

        return ans
