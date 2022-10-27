"""
DIFFICULTY : medium
TAGS : array, binary search, matrix, divide and conquer
"""
class Solution:
    # LOGIC : Search from top-right corner. Reduce 
    # the search space by one row or one column every time.
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        if(mat) :
            m, n = len(mat), len(mat[0])
            row, col = 0, n - 1
            while(row < m and col > 0) :
                if(mat[row][col] == target) :
                    return True
                elif(mat[row][col] > target) :
                    # DISCARD THE LAST COLUMN
                    col -= 1
                else :
                    # DISCARD THE FIRST ROW
                    row += 1
        
        return False