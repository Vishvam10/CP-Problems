from typing import List


def nQueens(n: int) -> List[List[int]]:
    if n == 1:
        return [[1]]

    def pp(mat):
        print("\n".join(["\t".join([str(cell) for cell in row]) for row in mat]))

    def flatten(mat):
        n, temp = len(mat), []
        for r in range(n):
            for c in range(n):
                temp.append(mat[r][c])
        return temp

    def isSafe(mat, row, col):
        # Same column ?
        r, c = row, col
        while r >= 0:
            if mat[r][col] == 1:
                return False
            r -= 1

        # Same upper left diagonal ?
        r, c = row, col
        while r >= 0 and c >= 0:
            if mat[r][c] == 1:
                return False
            r -= 1
            c -= 1

        # Same upper right diagonal ?
        r, c, n = row, col, len(mat)
        while r >= 0 and c < n:
            if mat[r][c] == 1:
                return False
            r -= 1
            c += 1

        return True

    def helper(mat, row, n, acc):
        if row == n:
            # pp(mat)
            acc.append(flatten(mat))
            return

        for col in range(n):
            check = isSafe(mat, row, col)
            if check:
                mat[row][col] = 1
                helper(mat, row + 1, n, acc)
                mat[row][col] = 0

        return acc

    mat = [[0 for i in range(n)] for j in range(n)]
    ans = helper(mat, 0, n, [])
    # print('ans : ', ans)

    return ans
