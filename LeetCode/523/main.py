"""
DIFFICULTY : medium
TAGS : array, hash table, math, prefix sum
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # initialize the hash map with index 0 for sum 0
        mp = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            # if the remainder s % k occurs for the first time
            if s % k not in mp:
                mp[s % k] = i + 1
            # if the subarray size is at least two
            elif mp[s % k] < i:
                return True
        return False
