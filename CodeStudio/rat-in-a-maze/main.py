from typing import List


def ratMaze(mat: List[List[int]]) -> List[str]:

    def solve(mat, row, col, pref, visited, acc):
        n = len(mat)

        if (row == n-1 and col == n-1):
            acc.append(pref)
            return acc

        # Left
        if (col-1 >= 0 and mat[row][col-1] == 1 and not visited[row][col-1]):
            visited[row][col] = True
            solve(mat, row, col-1, pref+'L', visited, acc)
            visited[row][col] = False

        # Right
        if (col+1 < n and mat[row][col+1] == 1 and not visited[row][col+1]):
            visited[row][col] = True
            solve(mat, row, col+1, pref+'R', visited, acc)
            visited[row][col] = False

        # Up
        if (row-1 >= 0 and mat[row-1][col] == 1 and not visited[row-1][col]):
            visited[row][col] = True
            solve(mat, row-1, col, pref+'U', visited, acc)
            visited[row][col] = False

        # Down
        if (row+1 < n and mat[row+1][col] == 1 and not visited[row+1][col]):
            visited[row][col] = True
            solve(mat, row+1, col, pref+'D', visited, acc)
            visited[row][col] = False

        return acc

    n = len(mat)
    vis = [[False for i in range(n)] for j in range(n)]
    if (mat[0][0] == 1):
        ans = solve(mat, 0, 0, '', vis, [])
    # print('ans : ', ans)

    return ans
