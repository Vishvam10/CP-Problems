class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        n = len(arr)
        mp = {}
        ans = 1
        for x in arr:
            if (x not in mp):
                mp[x] = 1
            else:
                mp[x] += 1
                if (mp[x] > n//2 and mp[x] > ans):
                    ans = x
        return ans
