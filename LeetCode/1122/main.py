"""
DIFFICULTY : medium
TAGS : array, hash table, sorting, counting sort
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = {}
        ans = []
        for i in range(len(arr1)):
            if arr1[i] in mp:
                mp[arr1[i]] += 1
            else:
                mp[arr1[i]] = 1

        for i in range(len(arr2)):
            for j in range(mp[arr2[i]]):
                ans.append(arr2[i])
                arr1.remove(arr2[i])
        if len(arr1) > 0:
            arr1.sort()
            ans += arr1

        return ans
