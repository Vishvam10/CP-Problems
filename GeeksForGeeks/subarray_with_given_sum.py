class Solution:
    def subArraySum(self,arr, n, s): 
       cur_sum = arr[0]
       start = 0
       i=1
        while i<=n:
            while cur_sum > s and start < i-1:
               cur_sum -= arr[start]
               start += 1
            if cur_sum == s:
               return [start+1,i]
            if i < n:
               cur_sum += arr[i]
            i += 1
        return [-1]