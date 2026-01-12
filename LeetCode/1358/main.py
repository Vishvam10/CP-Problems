class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ca, cb, cc = 0, 0, 0
        n, left, ans = len(s), 0, 0

        for i, ch in enumerate(s):
            if ch == "a":
                ca += 1
            elif ch == "b":
                cb += 1
            else:
                cc += 1

            while ca > 0 and cb > 0 and cc > 0:
                ans += n - i
                if s[left] == "a":
                    ca -= 1
                elif s[left] == "b":
                    cb -= 1
                else:
                    cc -= 1
                left += 1

        return ans
