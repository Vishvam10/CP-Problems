class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        n = len(arr)
        c, left, ans = 0, 0, 0

        for i in range(n):
            if arr[i] == 0:
                c += 1

            while c > k:
                if arr[left] == 0:
                    c -= 1
                left += 1

            ans = max(ans, i - left + 1)

        return ans
