class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(mat)
        m = len(mat[0])
        ind = []
        for i in range(n):
            for j in range(m):
                if (mat[i][j] == 0):
                    ind.append((i, j))

        for (i, j) in ind:

            # Set row to 0
            for it in range(n):
                mat[it][j] = 0

            # Set column to 0
            for it in range(m):
                mat[i][it] = 0
