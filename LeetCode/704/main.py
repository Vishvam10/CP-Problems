"""
DIFFICULTY : medium
TAGS : array, binary search
"""


class Solution:
    def search(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
