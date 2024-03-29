class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        left, ans = 0, 0

        for i in range(n+1):

            if (i - left != k):
                continue

            c = s[left:i]

            if (int(c) != 0 and num % int(c) == 0):
                ans += 1

            left += 1

        return ans
