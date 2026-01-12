class Solution:
    # Each element arr[i] is counted :
    # (i + 1) times (considering the left subarray : arr[0] to arr[i-1])
    # and (n - i) times (considering the right subarray : arr[i] to arr[n-1])
    # which is a total of : (i-1)*(n-1) times = k

    # No. of odd length subarrays = (k+1)/2  ==> What we want
    # No. of even length subarrays = k/2

    # So, arr[i] will be counted ((i + 1) * (n - i) + 1) // 2 times

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            ans += (((i + 1) * (n - i) + 1) // 2) * arr[i]
        return ans
