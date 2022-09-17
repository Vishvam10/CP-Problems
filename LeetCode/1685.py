class Solution:
    # nums[i] = a + b
    # a = nums[i]*i - (nums[0] + nums[1] + ... + nums[i-1])
    # b = (nums[i+1] + nums[i+2] + ... + nums[n-1]) - nums[i]*(n-i-1)
    # NOTE : |x-y| = max(x, y) - min(x, y)
    def getSumAbsoluteDifferences(self, arr: List[int]) -> List[int]:
        n = len(arr)
        pre = []
        suf = [None]*n
        ans = [None]*n
        s = 0
        for i in range(n) :
            s += arr[i]
            pre.append(s)
        s = 0
        for i in range(n-1, -1, -1) :
            s += arr[i]
            suf[i] = s
            
        for i in range(n) :
            ans[i] = (arr[i]*i - pre[i]) + (suf[i] - arr[i]*(n-i-1))
        
        return ans
            