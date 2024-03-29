from typing import *


def bitManipulation(n: int, i: int) -> List[int]:

    mask1 = 1
    res1 = n >> (i-1) & mask1

    mask2 = 1 << (i-1)
    res2 = n | mask2

    mask3 = ~(1 << (i-1))
    res3 = n & mask3

    return [res1, res2, res3]
