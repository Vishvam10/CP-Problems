"""
DIFFICULTY : easy
TAGS : array, simulation
"""


class Solution:
    def applyOperations(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = 0
        while i < n - 1:
            if arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
                i += 2
            else:
                i += 1

        last_zero_ind = 0

        for i, val in enumerate(arr):
            if val != 0:
                arr[last_zero_ind], arr[i] = arr[i], arr[last_zero_ind]
                last_zero_ind += 1

        return arr
