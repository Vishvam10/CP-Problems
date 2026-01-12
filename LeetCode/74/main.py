"""
DIFFICULTY : medium
TAGS : array, binary search, matrix
"""


class Solution:
    # ALTERNATE SOLUTION : Convert to 1D array directly
    # then binary search on it. There maybe overflow
    # because of n*m

    # n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
    # size n array convert to n * m matrix => a[x] =>matrix[x / m][x % m]

    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        def search(arr, target):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        rows, cols = len(mat[0]), len(mat)

        for i in range(cols):
            row = mat[i]
            if row[0] <= target and target <= row[rows - 1]:
                return search(row, target)
        return False
