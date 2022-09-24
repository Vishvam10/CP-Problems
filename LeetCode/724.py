"""
DIFFICULTY : easy
TAGS : array, prefix sum
"""
class Solution:
    # total sum = left_sum(i) + right_sum(i) - arr[i]
    #           = 2(left_sum(i)) - arr[i] ( as left_sum = right_sum)
    # TO FIND : If such i exists
    # SOLUTION : Either use a prefix sum to get left_sum or 
    #            calculate it on the go
    def pivotIndex(self, arr: List[int]) -> int:
        n = len(arr)
        ts = sum(arr)
        left_sum = 0
        for i in range(n) :
            if(left_sum == (ts - left_sum - arr[i])) :
                return i
            left_sum += arr[i]
        return -1
        