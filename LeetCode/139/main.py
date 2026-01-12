class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        def solve(pref):
            nonlocal ans
            if ans:
                return

            if n == len(pref):
                ans = True
                return

            for i in words:
                if ans:
                    return

                temp = pref + i

                if s.startswith(temp) and temp not in memo:
                    solve(temp)
                    memo.add(temp)

        ans = False
        memo = set()
        n = len(s)
        words.sort(key=lambda i: -len(i))

        solve("")

        return ans
