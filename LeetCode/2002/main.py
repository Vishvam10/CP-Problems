class Solution:
    def construct2DArray(self, arr: List[int], m: int, n: int) -> List[List[int]]:

        if (len(arr) != m * n):
            return []

        mat = [[0 for i in range(n)] for j in range(m)]
        row = 0

        for i in range(len(arr)):
            if (i != 0 and i % n == 0):
                row += 1

            mat[row][i % n] = arr[i]

        return mat
