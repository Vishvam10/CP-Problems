"""
DIFFICULTY : easy
TAGS : array, hash table, sorting
"""


class Solution:
    def countKDifference(self, arr: List[int], k: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) == k:
                    count += 1
        return count
