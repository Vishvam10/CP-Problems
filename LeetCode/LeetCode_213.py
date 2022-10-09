class Solution:
    # Exactly the same as House Robber (#198) but here we can't
    # consider both the first and the last house. But everything
    # else remains the same. In the end we take the maximum 
    #   1. Considering the first but not the last house and
    #   2. Considering the last but not the first house
    def rob(self, nums: List[int]) -> int:
        def helper(arr, i, j):
            if(len(arr) == 0) :
                return 0
            a = 0
            b = 0
            for ind in range(i, j) :
                temp = a
                a = max(a, b+arr[ind])
                b = temp
            return a

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            n = len(nums)
            return max(helper(nums, 1, n), helper(nums, 0, n-1))