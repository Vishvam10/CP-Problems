class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        # ans = [None]*len(arr)
        # ans[-1] = 0
        # for i in range(len(arr)-1) :
        #     max_diff = -10000000
        #     for j in range(i+1, len(arr)) :
        #         diff = arr[j] - arr[i]
        #         max_diff = max(max_diff, diff)
        #     ans[i] = max_diff
        # return max(ans)

        # n = len(arr)
        # left = 0
        # ans = 0
        # for i in range(1, n, 1) :
        #     if(arr[i] > arr[left]) :
        #         ans = max(ans, arr[i] - arr[left])
        #     else :
        #         left = i
        # return ans

        curSum, maxSum = 0, float("-inf")
        for i in range(1, len(arr)) :
            diff = arr[i] - arr[i-1]
            curSum += diff
            maxSum = max(maxSum, curSum)
            if(curSum < 0) :
                curSum = 0
        if(maxSum < 0) :
            return 0
        return maxSum
    
     