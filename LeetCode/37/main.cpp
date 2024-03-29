class Solution {
public:
  bool safe(int row, int col, vector<vector<char>> &board, char c) {
    for (int i = 0; i < 9; i++) {
      if (board[row][i] == c)
        return false;

      if (board[i][col] == c)
        return false;

      if (board[3 * (row / 3) + (i / 3)][3 * (col / 3) + (i % 3)] == c)
        return false;
    }
    return true;
  }

  bool solve(vector<vector<char>> &board) {
    int n = board[0].size();

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (board[i][j] == '.') {
          for (char digit = '1'; digit <= '9'; digit++) {
            if (safe(i, j, board, digit)) {
              // Set the state
              board[i][j] = digit;

              // Goto the next state
              bool possible = solve(board);

              // If next state can be solved
              if (possible) {
                return true;
              } else {
                // Reset the state
                board[i][j] = '.';
              }
            }
          }
          return false;
        }
      }
    }
    return true;
  }
  void solveSudoku(vector<vector<char>> &sudoku) { solve(sudoku); }
};