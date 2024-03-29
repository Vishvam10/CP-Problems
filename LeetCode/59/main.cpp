class Solution {
public:
  vector<vector<int>> generateMatrix(int n) {
    int left = 0, right = n - 1;
    int top = 0, bottom = n - 1;
    int x = 1;

    vector<vector<int>> mat(n, vector<int>(n, 0));

    while (left <= right && top <= bottom) {

      // go right
      for (int i = left; i <= right; i++) {
        mat[top][i] = x;
        x++;
      }

      top++;

      // go down
      for (int i = top; i <= bottom; i++) {
        mat[i][right] = x;
        x++;
      }

      right--;

      if (top <= bottom) {
        // go left
        for (int i = right; i >= left; i--) {
          mat[bottom][i] = x;
          x++;
        }

        bottom--;
      }

      if (left <= right) {
        // go up
        for (int i = bottom; i >= top; i--) {
          mat[i][left] = x;
          x++;
        }
        left++;
      }
    }

    return mat;
  }
};