class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        c = start = 0
        ans = []
        for i in range(n) :
            if(s[i] == '(') :
                c += 1
            else :
                c -= 1
                if(c == 0) :
                    ans.append(s[start+1:i])
                    start = i+1
    
        return ''.join(ans)
                
                    

                    

