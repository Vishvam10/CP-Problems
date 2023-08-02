class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        ans = ''
        if(n == 1):
            return s
        if(n == 2) :
            if(s[0] == s[1]) :
                return s
            else :
                return s[0]
        for i in range(n) :
            for j in range(i, n, 1) :
                temp = s[i:j+1]
                if(temp == temp[::-1] and len(temp) >= maxLen) :
                    ans = temp
                    maxLen = len(temp)
        
        return ans
