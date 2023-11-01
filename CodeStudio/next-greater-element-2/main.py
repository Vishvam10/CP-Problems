
from typing import List
from collections import deque

def nextGreaterElementII(arr: List[int]) -> List[int]:
    
    n = len(arr)
    ans = [-1] * n
    st = deque()

    for i in range(2*n-1, -1, -1) :

        while(len(st) > 0 and arr[i % n] >= st[-1]) :
            st.pop()
        
        if(i < n) :
            ans[i] = st[-1] if len(st) > 0 else -1
        
        st.append(arr[i % n])
    
    return ans

    