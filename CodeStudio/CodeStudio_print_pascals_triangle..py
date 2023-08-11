from typing import *

def pascalTriangle(nrows : int) -> List[List[int]]:
    ans = []
    ans.append([1])
    depth = 1
    while(depth < nrows) :
        temp = []
        temp.append(1)
        n = len(ans[len(ans)-1])
        for i in range(1, n, 1) :
            temp.append(ans[n-1][i-1] + ans[n-1][i])
        temp.append(1)
        ans.append(temp)
        depth += 1

    return ans