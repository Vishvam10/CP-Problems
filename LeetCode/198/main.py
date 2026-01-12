class Solution:
    def rob(self, arr: List[int]) -> int:
        def solve(ind):
            if ind < 0:
                return 0

            if mp[ind] >= 0:
                return mp[ind]

            yes = arr[ind] + solve(ind - 2)
            no = solve(ind - 1)
            ans = max(yes, no)

            mp[ind] = ans

            return ans

        n = len(arr)
        mp = [-1 for i in range(n + 1)]
        ans = solve(n - 1)

        return ans
