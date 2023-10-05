class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n, pm = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                pm += 4*grid[i][j]
                if i > 0:   pm -= grid[i][j]*grid[i-1][j]
                if i < m-1: pm -= grid[i][j]*grid[i+1][j]
                if j > 0:   pm -= grid[i][j]*grid[i][j-1]
                if j < n-1: pm -= grid[i][j]*grid[i][j+1]
                    
        return pm
