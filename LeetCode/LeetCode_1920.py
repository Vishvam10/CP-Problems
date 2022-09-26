"""
DIFFICULTY : easy
TAGS : array, simulation
"""
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0 for x in nums]
        for i in range(0, len(nums)) :
            ans[i] = nums[nums[i]]
        return ans
        