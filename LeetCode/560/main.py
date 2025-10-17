class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        s = 0
        ans = 0
        mp = defaultdict(int)
        mp[0] = 1

        for x in arr:
            s += x
            target = s - k
            ans += mp[target]
            mp[s] += 1

        return ans