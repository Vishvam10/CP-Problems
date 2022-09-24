"""
DIFFICULTY : medium
TAGS : array, dp, greedy
"""
class Solution:
    # A bit similar to Kadane's Algorithm
    def canJump(self, arr: List[int]) -> bool:
        n = len(arr)
        max_pos = 0
        i = 0
        while(i <= max_pos) :       
            max_pos = max(max_pos, i + arr[i])
            if(max_pos >= n - 1) :
                return True
            i += 1
        return False