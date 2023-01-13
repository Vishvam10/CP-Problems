"""
DIFFICULTY : easy
TAGS : math, simulation
"""
class Solution:
    def countEven(self, n: int) -> int:
        def ds(n) :         
            s = 0
            while(n > 0) :
                rem = n % 10
                s += rem
                n //= 10
            return s
        ans = 0
        for i in range(1, n+1) :
            if(ds(i) % 2 == 0) :
                ans += 1
        return ans