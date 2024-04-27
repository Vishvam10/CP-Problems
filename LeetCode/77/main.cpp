class Solution {
public:
  vector<vector<int>> ans;

  void solve(vector<int> &arr, vector<int> &path, int start, int choices) {
    if (choices == 0) {
      ans.emplace_back(path);
      return;
    }

    for (int i = start; i < arr.size(); i++) {

      // set the state
      path.emplace_back(arr[i]);

      // goto next state
      solve(arr, path, i + 1, choices - 1);

      // reset the state
      path.pop_back();
    }

    return;
  }

  vector<vector<int>> combine(int n, int k) {
    vector<int> arr(n);
    vector<int> path;

    iota(arr.begin(), arr.end(), 1);

    solve(arr, path, 0, k);

    return ans;
  }
};