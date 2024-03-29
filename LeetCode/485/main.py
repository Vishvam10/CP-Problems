class Solution:
    def findMaxConsecutiveOnes(self, arr: List[int]) -> int:
        n = len(arr)
        c = ans = 0
        for i in range(n):
            if (arr[i] == 1):
                c += 1
            else:
                ans = max(ans, c)
                c = 0
        ans = max(ans, c)
        return ans
