class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        mp = {}
        ans = []
        for arr in nums:
            for x in arr:
                if x in mp:
                    mp[x] += 1
                else:
                    mp[x] = 1
        for k, v in mp.items():
            if v == len(nums):
                ans.append(k)
        ans.sort()
        return ans
