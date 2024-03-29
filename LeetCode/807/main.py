"""
DIFFICULTY : medium
TAGS : array, greedy, matrix
"""


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [0 for x in grid[0]]
        col_max = [0 for x in grid[0]]
        ans = 0
        for i in range(0, n):
            for j in range(0, n):
                row_max[i] = max(row_max[i], grid[i][j])

        for i in range(0, n):
            for j in range(0, n):
                col_max[i] = max(col_max[i], grid[j][i])

        for i in range(0, n):
            row_mx = row_max[i]
            for j in range(0, n):
                diff = min(row_mx, col_max[j]) - grid[i][j]
                ans += diff
        return ans
