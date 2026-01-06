class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        curSum = 0
        maxSum = float("-inf")
        
        for i in range(len(arr)) :
            curSum = max(arr[i], curSum + arr[i])
            maxSum = max(maxSum, curSum)
        
        return maxSum    