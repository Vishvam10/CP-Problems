class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0

        for i in range(n):
            ans += mat[i][i]
            if (i != n-i-1):
                ans += mat[n-i-1][i]

        return ans
