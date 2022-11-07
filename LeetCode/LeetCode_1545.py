"""
DIFFICULTY : medium
TAGS : string, recursion
"""
class Solution:
    def invert(self, s) :
        res = []
        for ch in list(s) :
            if(ch == "0") :
                res.append("1")
            else :
                res.append("0")
        return "".join(res)

    def rev(self, s) :
        return s[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        
        def helper(count, limit, s) :
            if(count == limit) :
                return s
            else :
                new_str = s + "1" + self.rev(self.invert(s))
                return helper(count + 1, limit, new_str)
        
        if(n == 1) :
            return "0"
        
        s = helper(1, n, "0")
        return s[k-1]
                
        