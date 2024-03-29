class Solution {
public:
  int diagonalSum(vector<vector<int>> &mat) {
    int n = mat.size(), ans = 0;
    // i == j and i + j == n - 1

    for (int i = 0; i < n; i++) {
      ans += mat[i][i];

      // to exclude the middle element
      if (i != n - i - 1) {
        ans += mat[n - i - 1][i];
      }
    }

    return ans;
  }
};