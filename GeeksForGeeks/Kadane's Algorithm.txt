import math
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr, n):
        max_sum = -math.inf
        cur_sum = 0
        for i in range(n) :
            cur_sum += arr[i]
            if(cur_sum > max_sum) :
                max_sum = cur_sum
            if(cur_sum < 0) :
                cur_sum = 0
        return max_sum