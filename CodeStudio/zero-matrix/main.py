def zeroMatrix(mat, n, m):
    # Write your code here.
    n = len(mat)
    m = len(mat[0])
    ind = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                ind.append((i, j))

    for i, j in ind:
        # Set row to 0
        for it in range(n):
            mat[it][j] = 0

        # Set column to 0
        for it in range(m):
            mat[i][it] = 0

    return mat
