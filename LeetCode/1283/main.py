import math


class Solution:
    def smallestDivisor(self, arr: List[int], t: int) -> int:
        n = len(arr)
        if n > t:
            return -1
        low, high = 1, max(arr)

        def sd(arr, div):
            s = 0
            for i in range(len(arr)):
                s += math.ceil(arr[i] / div)
            return s

        while (low <= high):
            mid = low + (high - low) // 2
            val = sd(arr, mid)
            if (val <= t):
                high = mid - 1
            else:
                low = mid + 1

        return low
