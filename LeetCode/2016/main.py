"""
DIFFICULTY : easy
TAGS : array
"""
class Solution:
    # Initialize mn = 0 and start from i = 1
    # This guarantees the j > i condition
    def maximumDifference(self, arr: List[int]) -> int:
        mn, ans = arr[0], -1
        for i in range(1, len(arr)) :
            ans = max(ans, arr[i] - mn)
            mn = min(mn, arr[i])
        if(ans == 0) :
            return -1
        return ans
            
        