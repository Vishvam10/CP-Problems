void print_mat(vector<vector<int>> &mat) {

  for (const auto &row : mat) {
    for (int element : row) {
      cout << element << " ";
    }
    cout << "\n";
  }
}

class Solution {
public:
  vector<vector<int>> ans;

  void solve(vector<int> &arr, int target, int start, vector<int> path) {

    if (target < 0) {
      return;
    }

    if (target == 0) {
      ans.emplace_back(path);
      return;
    }

    for (int i = start; i < arr.size(); i++) {

      // consider the element (again, if needed)
      path.emplace_back(arr[i]);

      // goto next state
      solve(arr, target - arr[i], i, path);

      // reset the state
      path.pop_back();
    }
    return;
  }

  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    vector<int> path;
    solve(candidates, target, 0, path);

    // print_mat(ans);

    return ans;
  }
};