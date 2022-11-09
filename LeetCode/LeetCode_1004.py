"""
DIFFICULTY : medium
TAGS : array, sliding window, binary search, prefix sum
"""
class Solution:
    # IDEA : Find the longest subarray with at most K zeros.
    # APPROACH : 
    #   - For each A[right], try to find the longest subarray.
    #   - If A[left] ~ A[right] has zeros <= K, we continue to increment left.
    #   - If A[left] ~ A[right] has zeros > K, we increment left (as well as right).
    
    def longestOnes(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left = 0
        for right in range(n) :
            # Equivalent to move right if 0 is present
            k -= (1 - arr[right])
            if k < 0 :
                k += (1 - arr[left])
                left += 1
        return right - left + 1
                