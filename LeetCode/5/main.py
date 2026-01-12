class Solution:
    def longestPalindrome(self, s: str) -> str:
        def solve(start, end):
            if start == end:
                return True

            if end - start == 1:
                return s[start] == s[end]

            if (start, end) in mp:
                return mp[(start, end)]

            if s[start] != s[end]:
                return False

            ans = solve(start + 1, end - 1)
            mp[(start, end)] = ans

            return ans

        left, right = 0, 1
        n = len(s)
        mp = {}
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (j - i + 1) > right - left and solve(i, j):
                    left, right = i, j + 1

        return s[left:right]
