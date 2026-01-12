from typing import *


def superiorElements(a: List[int]) -> List[int]:
    # # Write your code here.
    # n = len(a)
    # ans = []
    # ans.append(a[-1])
    # temp = [0]*n
    # temp[-1] = a[-1]

    # for i in range(n-2, -1, -1) :
    #     if(temp[i+1] >= a[i]) :
    #         temp[i] = temp[i+1]
    #     else :
    #         temp[i] = a[i]
    #         ans.append(a[i])

    # # print('temp : ', temp)
    # return ans

    n = len(a)
    ans = []
    ans.append(a[-1])
    mx = a[-1]
    for i in range(n - 2, -1, -1):
        if a[i] > mx:
            ans.append(a[i])
            mx = a[i]

    # print('temp : ', temp)
    return ans
