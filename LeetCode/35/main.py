"""
DIFFICULTY : easy
TAGS : array, binary search
"""


class Solution:
    def searchInsert(self, arr: List[int], x: int) -> int:

        def ub(arr, n, x):
            left = 0
            right = n - 1
            ans = 0
            while (left <= right):
                mid = left + (right - left) // 2
                if (arr[mid] == x):
                    ans = mid
                    left = mid + 1
                elif (arr[mid] < x):
                    ans = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        return ub(arr, len(arr), x)
