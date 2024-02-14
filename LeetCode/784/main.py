class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def helper(s, pos) :

            if(pos == len(s)) :
                ans.append(s)
                return
            
            if(not s[pos].isalpha()) :
                helper(s, pos + 1)
            
            elif(s[pos].isupper()) :
                helper(s, pos + 1)
                temp = s[:pos] + s[pos].lower() + s[pos+1:]
                helper(temp, pos + 1)
            else :
                helper(s, pos + 1)
                temp = s[:pos] + s[pos].upper() + s[pos+1:]
                helper(temp, pos + 1)

            return

        ans = []

        helper(s, 0)

        return ans