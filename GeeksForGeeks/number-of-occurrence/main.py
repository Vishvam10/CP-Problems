"""
DIFFICULTY : basic
TAGS : array, searching
"""


class Solution:

    def count(self, arr, n, target):
        # code here
    if (n == 0):
        return 0

    def FIRST(arr, low, high, target):
        res = -1
        while low <= high:
            mid = low + (high - low) // 2
            if (arr[mid] == target):
                res = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return res

    def LAST(arr, low, high, target):
        res = -1
        while (low <= high):
            mid = low + (high - low) // 2
            if (arr[mid] == target):
                res = mid
                low = mid + 1
            elif (arr[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        return res

    first = FIRST(arr, 0, n-1, target)
    last = LAST(arr, 0, n-1, target)

    if (first != -1 and last != -1):
        return last - first + 1
    else:
        return 0
