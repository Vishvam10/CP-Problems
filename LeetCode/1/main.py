"""
DIFFICULTY : easy
TAGS : array, hash table
"""


class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(arr)):
            x = target - arr[i]
            if x in mp:
                return [mp[x], i]
            mp[arr[i]] = i
