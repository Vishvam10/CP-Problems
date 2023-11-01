from typing import *

def countGreater(n: int, m: int, arr: List[int], query: List[int]) -> List[int]:
     
    ans = [0] * m

    for q in range(m) :
        c = 0
        for i in range(n-1, query[q], -1) :
            if(arr[i] > arr[query[q]]) :
                c += 1

        ans[q] = c

    return ans    
        