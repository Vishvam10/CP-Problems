class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        n = len(arr)
        left, prod, ans = 0, 1, 0
        for i in range(n):
            prod *= arr[i]
            while left <= i and prod >= k:
                prod //= arr[left]
                left += 1

            ans += i - left + 1

        return ans
