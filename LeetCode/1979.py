class Solution:
    def gcd(a, b) :
        if(a == 0) :
            return b
        return gcd(b%a, a)
    
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))
        