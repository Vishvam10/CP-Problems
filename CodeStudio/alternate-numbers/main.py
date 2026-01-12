from typing import *


def alternateNumbers(arr: List[int]) -> List[int]:
    n = len(arr)
    pos = []
    neg = []
    ans = []
    left = right = 0
    for x in arr:
        if x > 0:
            pos.append(x)
        else:
            neg.append(x)

    for i in range(n // 2):
        ans.append(pos[i])
        ans.append(neg[i])

    return ans
