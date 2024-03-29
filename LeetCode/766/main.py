"""
DIFFICULTY : easy
TAGS : array, matrix
"""


class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i > 0 and j > 0 and mat[i-1][j-1] != mat[i][j]):
                    return False
        return True

        # return all(
        #             r == 0 or c == 0 or mat[r-1][c-1] == val
        #             for r, row in enumerate(mat)
        #             for c, val in enumerate(row)
        #           )
