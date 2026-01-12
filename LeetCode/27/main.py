"""
DIFFICULTY : easy
TAGS : array, two pointers
"""


class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        j = 0
        for i in range(len(arr)):
            if arr[i] != val:
                arr[j] = arr[i]
                j += 1
        return j
