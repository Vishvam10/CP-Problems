class Solution {
public:
  int countNegatives(vector<vector<int>> &arr) {
    int n = arr.size();
    int m = arr[0].size();

    int row = 0, col = m - 1, ans = 0;
    // if arr[row][col] < 0, then entire col < 0
    // so, we can just add (n - row) and skip the col

    while (row <= n - 1 && col >= 0) {
      int ele = arr[row][col];
      if (ele < 0) {
        ans += (n - row);
        col--;
      } else {
        row++;
      }
    }

    return ans;
  }
};