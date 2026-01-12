"""
DIFFICULTY : easy
TAGS : array, hash table
"""


class Solution:
    def findMaxK(self, arr: List[int]) -> int:
        arr.sort()
        left = 0
        right = len(arr) - 1
        ans = -1
        while left < right:
            if arr[left] + arr[right] == 0:
                ans = max(ans, arr[right])
                left += 1
                right -= 1
            elif arr[left] + arr[right] > 0:
                right -= 1
            else:
                left += 1

        return ans
