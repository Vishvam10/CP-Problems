def countSetBits(n: int) -> int:
    
    ans = 0

    for i in range(1, n+1) :
        res = 0
        while(i != 0) :
            i &= (i-1)
            res += 1
        ans += res
    
    return ans



 