import math


class Solution:
    def minEatingSpeed(self, arr: List[int], max_hours: int) -> int:

        if (len(arr) == max_hours):
            return max(arr)

        def check(arr, val):
            temp = 0
            for i in range(len(arr)):
                temp += math.ceil(arr[i] / val)
            return temp

        low, high = 1, max(arr)
        while (low <= high):
            mid = low + (high - low) // 2
            hours = check(arr, mid)
            if (hours <= max_hours):
                high = mid - 1
            else:
                low = mid + 1
        return low
