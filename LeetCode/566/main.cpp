class Solution {
public:
  vector<vector<int>> matrixReshape(vector<vector<int>> &arr, int r, int c) {

    int n = arr.size();
    int m = arr[0].size();

    if (r * c != m * n) {
      return arr;
    }

    vector<vector<int>> mat(r, vector<int>(c, 0));
    int row = 0, col = 0;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (col > c - 1) {
          col = 0;
          row++;
        }
        mat[row][col] = arr[i][j];
        col++;
      }
    }

    /*
        OR

        int count = 0

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                mat[count / c][count % c] = arr[i][j];
                count++;
            }
        }
    */

    return mat;
  }
};