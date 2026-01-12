"""
DIFFICULTY : easy
TAGS : array, string
"""


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # arr = [len(x) for x in nums]
        # k = len(target)
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    count += 1
        return count
