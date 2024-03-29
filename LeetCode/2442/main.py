"""
DIFFICULTY : medium
TAGS : array, hash table, math
"""


class Solution:
    def countDistinctIntegers(self, arr: List[int]) -> int:
        def rev(n):
            ans = 0
            while (n):
                ans = (ans * 10) + n % 10
                n //= 10
            return ans
        temp = []
        mp = {}
        ans = 0
        for x in arr:
            temp.append(rev(x))
        arr.extend(temp)
        for i, x in enumerate(arr):
            if (x not in mp):
                mp[x] = i
        for k in mp.keys():
            ans += 1

        return ans
