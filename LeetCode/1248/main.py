class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:

        def atmost(arr, k):
            n = len(arr)
            left, ans = 0, 0

            for i in range(n):

                if (arr[i] % 2 == 1):
                    k -= 1

                while (k < 0):
                    if (arr[left] % 2 == 1):
                        k += 1
                    left += 1

                ans += (i - left + 1)

            return ans

        return atmost(arr, k) - atmost(arr, k-1)
