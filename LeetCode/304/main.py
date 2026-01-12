class NumMatrix:
    def __init__(self, mat: List[List[int]]):
        n = len(mat)
        m = len(mat[0])

        self.pref = [[0 for i in range(m)] for j in range(n)]
        self.pref[0][0] = mat[0][0]

        # Set the 1st row and column
        for i in range(m):
            self.pref[0][i] = self.pref[0][i - 1] + mat[0][i]

        for i in range(n):
            self.pref[i][0] = self.pref[i - 1][0] + mat[i][0]

        for row in self.pref:
            print(row)

        for i in range(1, n, 1):
            for j in range(1, m, 1):
                self.pref[i][j] = (
                    mat[i][j]
                    + self.pref[i - 1][j]
                    + self.pref[i][j - 1]
                    - self.pref[i - 1][j - 1]
                )

    def getVal(self, row, col):
        if row < 0 or col < 0:
            return 0
        return self.pref[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.getVal(row2, col2)
        a = self.getVal(row1 - 1, col1 - 1)
        b = self.getVal(row1 - 1, col2)
        c = self.getVal(row2, col1 - 1)

        return s + a - b - c


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
