"""
DIFFICULTY : medium
TAGS : array, matrix, simulation
"""


class Solution:
    def spiralOrder(self, arr: List[List[int]]) -> List[int]:
        ans = []
        if len(arr) == 0:
            return ans
        row_begin = 0
        col_begin = 0
        row_end = len(arr)-1
        col_end = len(arr[0])-1
        while (row_begin <= row_end and col_begin <= col_end):

            # GO RIGHT
            for i in range(col_begin, col_end + 1):
                ans.append(arr[row_begin][i])
            row_begin += 1

            # GO DOWN
            for i in range(row_begin, row_end + 1):
                ans.append(arr[i][col_end])
            col_end -= 1

            # GO LEFT
            if (row_begin <= row_end):
                for i in range(col_end, col_begin - 1, -1):
                    ans.append(arr[row_end][i])
                row_end -= 1

            # GO UP
            if (col_begin <= col_end):
                for i in range(row_end, row_begin - 1, -1):
                    ans.append(arr[i][col_begin])
                col_begin += 1

        return ans
