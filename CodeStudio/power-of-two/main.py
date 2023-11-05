def isPowerOfTwo(n: int) -> bool:
    
    mask = (n-1)
    res = ~(n & mask)

    return res