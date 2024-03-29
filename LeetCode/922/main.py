"""
DIFFICULTY : easy
TAGS : array, two pointers, sorting
"""


class Solution:
    # IDEA : For every misplaced odd element, there is a misplaced even
    #        element since there are is just enough space for
    #        both odds and evens

    def sortArrayByParityII(self, arr: List[int]) -> List[int]:
        i, j, n = 0, 1, len(arr)
        while j < n and i < n:
            if arr[i] % 2 == 0:
                i += 2
            elif arr[j] % 2 == 1:
                j += 2
            else:
                arr[i], arr[j] = arr[j], arr[i]
        return arr
