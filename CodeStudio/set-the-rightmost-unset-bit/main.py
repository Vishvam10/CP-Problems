from typing import *


def setBits(n: int) -> int:
    if n & (n + 1) == 0:
        return n

    return n | (n + 1)
