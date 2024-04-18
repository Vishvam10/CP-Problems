class Solution {
public:
  int ans = 0;

  bool check(vector<vector<int>> &mat, int x, int y) {

    int n = mat.size();

    for (int i = 0; i < n; i++) {
      if (mat[x][i] == 1 || mat[i][y] == 1) {
        return false;
      }
    }

    int i = x, j = y;
    while (i >= 0 && j >= 0) {
      if (mat[i][j] == 1) {
        return false;
      }
      i--;
      j--;
    }

    i = x, j = y;
    while (i < n && j >= 0) {
      if (mat[i][j] == 1) {
        return false;
      }
      i++;
      j--;
    }

    return true;
  }

  void solve(vector<vector<int>> &mat, int col) {
    if (col == mat.size()) {
      ans++;
      return;
    }

    // go row wise
    for (int i = 0; i < mat.size(); i++) {

      if (check(mat, i, col)) {

        // set state
        mat[i][col] = 1;

        // goto next state
        solve(mat, col + 1);

        // reset the state
        mat[i][col] = 0;
      }
    }
    return;
  }

  int totalNQueens(int n) {

    vector<vector<int>> mat(n, vector<int>(n, 0));
    solve(mat, 0);

    return ans;
  }
};