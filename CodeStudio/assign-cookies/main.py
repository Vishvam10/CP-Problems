from typing import *


def assignCookie(greed: List[int], size: List[int]) -> int:
    greed.sort()
    size.sort()
    i, j = 0, 0
    while (i < len(greed) and j < len(size)):
        if (size[j] >= greed[i]):
            i += 1
        j += 1
    return i
