"""
DIFFICULTY : medium
TAGS : string
"""
class Solution:
    def countAndSay(self, num: int) -> str:
        
        def helper(s) :
            res = ""
            i = 0
            # We could use a stack but this is clearly better
            res = ""
            i = 0
            while(i < len(s)) :
                ch = s[i]
                count = 0
                while(i < len(s) and s[i] == ch) :
                    i += 1
                    count += 1
                res += str(count) + str(ch)
            
            return res
        
        if(num <= 0) :
            return "-1"
        
        ans = "1"
        
        for i in range(1, num) :
            ans = helper(ans)
            
        return ans
    