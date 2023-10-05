class Solution:
    # Note the first 0 and swap it with
    # occurring non-zero element
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)) :
            if(nums[i] != 0) :
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        