"""
DIFFICULTY : easy
TAGS : array, hash table, matrix
"""


class Solution:
    def checkValid(self, mat: List[List[int]]) -> bool:
        n = len(mat)
        for x in range(n):
            # Can also use normal arrays : [0] * (n+1)
            row = bytearray(n + 1)
            col = bytearray(n + 1)
            for y in range(n):
                r, c = mat[x][y], mat[y][x]
                row[r] += 1
                col[c] += 1
                if row[r] > 1 or col[c] > 1:
                    return False
        return True
