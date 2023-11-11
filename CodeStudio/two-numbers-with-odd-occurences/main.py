from typing import *

def twoOddNum(arr : List[int]) -> List[int]:
    
    '''
        
        res = (a ^ b)
        
        now, say res was 11001
        note that to get ____1 here, either :
            1. a would have 1 at that place and b would have 0 OR
            2. b would have 1 at that place and a would have 0
        
        we want to see the right most set bit (rmsb) of res 
        then, we split the arr into 2 parts :
            1. numbers that have 1 in rmsb  (res1)
            2. numbers that have 0 in rmsb  (res2)

        repeat the same procedure for to calculate res1 and res2
        like we did for res

    '''
    
    n = len(arr)
    res, res1, res2 = 0, 0, 0

    for x in arr :
        res ^= x

    rmsb = res & ~(res - 1)

    for x in arr :
        if(x & rmsb) :
            res1 ^= x
        else :
            res2 ^= x
    
    return [max(res1, res2), min(res1, res2)]
    
    

    