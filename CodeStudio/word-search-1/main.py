from typing import List


def present(board: List[List[str]], word: str, n: int, m: int) -> bool:

    def solve(x, y, n, m, board, word, ind):
        if (ind == len(word)):
            return True

        if ((x < 0 or x == n) or (y < 0 or y == m) or (board[x][y] != word[ind])):
            return False

        temp = board[x][y]

        # Set state
        board[x][y] = '#'   # Some dummy value

        # Goto next state
        left = solve(x, y-1, n, m, board, word, ind+1)
        right = solve(x, y+1, n, m, board, word, ind+1)
        up = solve(x-1, y, n, m, board, word, ind+1)
        down = solve(x+1, y, n, m, board, word, ind+1)

        # Reset state
        board[x][y] = temp

        return (left or right or up or down)

    for i in range(n):
        for j in range(m):
            if (board[i][j] == word[0]):
                print('reached')
                check = solve(i, j, n, m, board, word, ind)
                if (check):
                    return True

    return False
