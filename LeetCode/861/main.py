"""
DIFFICULTY : medium
TAGS : array, matrix, greedy, bit manipulation
"""


class Solution:
    # IDEA :
    #   - Make sure the bits from left side are set i.e. 1
    #   - Flip all rows where first element is 0
    #   - Flip all columns where the number
    #     of 1s < number of 0s

    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for x in range(rows):
            if grid[x][0] == 0:
                for y in range(cols):
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                    else:
                        grid[x][y] = 0

        for y in range(cols):
            temp = 0
            for x in range(rows):
                if grid[x][y] == 1:
                    temp += 1

            # Less 1s than 0s
            if temp < rows - temp:
                for x in range(rows):
                    if grid[x][y] == 1:
                        grid[x][y] = 0
                    else:
                        grid[x][y] = 1

        ans = 0

        # Can also do sum([int("".join(row), 2) for row in grid])

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    ans += 2 ** (cols - y - 1)

        return ans
