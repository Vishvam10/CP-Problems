"""
DIFFICULTY : easy
TAGS : binary search, interactive
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                high = mid - 1
        return low
