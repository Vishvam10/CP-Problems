from typing import List

def missingNumber(n: int, arr: List[int]) -> int:
    ans = 0
    for x in arr :
        ans ^= x
    return ans