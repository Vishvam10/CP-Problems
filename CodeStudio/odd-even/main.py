from typing import *


def oddEven(n: int) -> str:

    mask = 1
    res = n & mask
    return 'odd' if res else 'even'
