"""
DIFFICULTY : easy
TAGS : array, hash table, counting
"""


class Solution:
    def sumOfUnique(self, arr: List[int]) -> int:
        mp = {}
        ans = 0
        for x in arr:
            if x in mp:
                mp[x] += 1
            else:
                mp[x] = 1
        for k, v in mp.items():
            if v == 1:
                ans += k

        return ans
