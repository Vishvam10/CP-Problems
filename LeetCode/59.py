"""
DIFFICULTY : medium
TAGS : array, matrix, simulation
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        ans = [[0 for _ in range(n)] for _ in range(n)]
        row_begin, row_end, col_begin, col_end, num = 0, n-1, 0, n-1, 1
        while row_begin <= row_end and col_begin <= col_end:
            # GO RIGHT
            for i in range(row_begin, row_end+1):
                ans[col_begin][i] = num 
                num += 1
            col_begin += 1
            
            # GO DOWN
            for i in range(col_begin, col_end+1):
                ans[i][row_end] = num
                num += 1
            row_end -= 1
            
            # GO LEFT
            for i in range(row_end, row_begin-1, -1):
                ans[col_end][i] = num
                num += 1
            col_end -= 1
            
            # GO UP
            for i in range(col_end, col_begin-1, -1):
                ans[i][row_begin] = num
                num += 1
            row_begin += 1
            
        return ans
        