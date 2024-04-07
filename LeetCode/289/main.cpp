class Solution {
public:
  int liveNeighbors(vector<vector<int>> &mat, int i, int j, int m, int n) {
    int ans = 0;
    int offsets[8][2] = {{-1, 0},  {1, 0},  {0, -1}, {0, 1},
                         {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};

    for (int k = 0; k < 8; k++) {
      int ni = i + offsets[k][0];
      int nj = j + offsets[k][1];
      if (ni >= 0 && ni < m && nj >= 0 && nj < n &&
          (mat[ni][nj] == 1 || mat[ni][nj] == 3)) {
        ans++;
      }
    }

    return ans;
  }

  void gameOfLife(vector<vector<int>> &mat) {
    int m = mat.size();
    int n = mat[0].size();

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        int live = liveNeighbors(mat, i, j, m, n);
        if (mat[i][j] == 0) {
          if (live == 3) {
            // mark as alive
            mat[i][j] = 2;
          }
        } else if (mat[i][j] == 1) {
          if (live < 2 || live > 3) {
            // mark as dead
            mat[i][j] = 3;
          }
        }
      }
    }

    // resolve marked entries

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 2) {
          mat[i][j] = 1; // Set to alive
        } else if (mat[i][j] == 3) {
          mat[i][j] = 0; // Set to dead
        }
      }
    }
  }
};
