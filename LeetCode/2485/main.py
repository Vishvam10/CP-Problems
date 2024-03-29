"""
DIFFICULTY : easy
TAGS : math, prefix sum
"""


class Solution:
    def pivotInteger(self, n: int) -> int:
        s = (n * (n+1)) // 2
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            cur = (mid * (mid+1))//2
            key = s - cur + mid
            if cur == key:
                return mid
            elif cur < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1
