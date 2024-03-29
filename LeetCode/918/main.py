class Solution:
    # Find the A: max subarray sum and B: min subarray sum. The ans
    # is the max(A, total_sum - B)

    # See this: https://assets.leetcode.com/users/motorix/image_1538888300.png

    # NOTE : A smaller min subarray can not form because the max
    #        subarray would gobble the extra elements anyway
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, arr[0], 0, arr[0], 0
        for a in arr:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
