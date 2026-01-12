class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        def helper(pos, res):
            key = (pos, res)

            if key not in mp:
                if pos == len(arr):
                    return 1 if res == target else 0
                else:
                    # pick +
                    a = helper(pos + 1, res + arr[pos])

                    # pick -
                    b = helper(pos + 1, res - arr[pos])

                    mp[key] = a + b

            return mp[key]

        mp = defaultdict(int)
        ans = helper(0, 0)

        print(ans)

        return ans
