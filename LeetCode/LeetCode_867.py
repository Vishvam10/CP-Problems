"""
DIFFICULTY : medium
TAGS : array, matrix, simulation
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        ans = [[0 for i in range(n)] for j in range(m)]
        for i in range(m) :
            for j in range(n) :
                ans[i][j] = matrix[j][i]
        return ans
                