def isKthBitSet(n: int, k: int) -> bool:

    mask = 1 << (k-1)
    return n & mask
