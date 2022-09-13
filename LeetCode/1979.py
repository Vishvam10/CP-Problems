class Solution:
    def gcd(self, a, b) :
        if(a == 0) :
            return b
        return self.gcd(b%a, a)
    
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(min(nums), max(nums))
        