class Solution:
    def MissingNumber(self, arr, n):
        return int(((n*n + n)/2) - sum(arr))
