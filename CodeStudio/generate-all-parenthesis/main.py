def validParenthesis(n: int) -> int:
    
    def helper(s, op, cl, n, acc) :
        if(len(s) == 2*n) :
            acc.append(s)
            return
        if(op < n) :
            helper(s+'(', op+1, cl, n, acc)
        
        if(cl < op) :
            helper(s+')', op, cl+1, n, acc)
        
        return acc
    
    ans = helper('', 0, 0, n, [])
    return ans

