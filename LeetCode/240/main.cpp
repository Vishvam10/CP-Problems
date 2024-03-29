class Solution {
public:
  bool searchMatrix(vector<vector<int>> &arr, int target) {

    int n = arr.size();
    int m = arr[0].size();
    int row = 0, col = m - 1, ele;

    while (row <= n - 1 && col >= 0) {
      ele = arr[row][col];
      if (ele == target) {
        return true;
      } else if (ele > target) {
        // go left
        col--;
      } else {
        // go down
        row++;
      }
    }
    return false;
  }
};