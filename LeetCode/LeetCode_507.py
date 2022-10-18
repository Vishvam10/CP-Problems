"""
DIFFICULTY : easy
TAGS : math
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
                
        ans = 1
        
        for i in range(2, floor(num**0.5) + 1):
            if num % i == 0:
                if i == num // i :
                    # square root, should only add once
                    ans +=  i
                else:
                    # add factor i and (num // i)
                    ans += ( i + num // i )
                    
        return ans == num