class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        ans = 0
        for x in arr:
            ans ^= x
        return ans
