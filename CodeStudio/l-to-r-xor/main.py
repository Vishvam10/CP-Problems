from typing import *


def findXOR(l: int, r: int) -> int:
    '''
    1         1           [0001]
    2        10           [0011]

    3        11           [0000]   <--- Equal to 0
    4       100           [0100]  
    5       101           [0001]
    6       110           [0111]

    7       111           [0000]   <--- Equal to 0
    8      1000           [1000]  
    9      1001           [0001]
    10     1010           [1011]

    11     1011           [0000]   <--- Equal to 0
    12     1100           [1100]  

    '''

    def xor(n):

        rem = n & 3    # rem = n % 4

        if (rem == 0):
            return n
        elif (rem == 1):
            return 1
        elif (rem == 2):
            return n + 1
        else:
            return 0

    mask1 = xor(l-1)
    mask2 = xor(r)
    ans = mask1 ^ mask2     # Cancels 1 to (l-1)
    return ans
