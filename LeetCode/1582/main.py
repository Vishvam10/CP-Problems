class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = [0]*m, [0]*n
        ans = 0

        for i in range(m) :
            for j in range(n) :
                rows[i] += mat[i][j]
                cols[j] += mat[i][j]
        
        for i in range(m) :
            for j in range(n) :
                ans += (mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1)
        
        return ans