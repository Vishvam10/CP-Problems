class Solution {
public:
  vector<vector<int>> ans;
  unordered_map<string, bool> mp;

  void solve(vector<int> &arr, int target, int start, vector<int> &path) {

    if (target < 0) {
      return;
    }

    if (target == 0) {
      ans.emplace_back(path);
      return;
    }

    for (int i = start; i < arr.size(); i++) {

      // avoiding duplicates
      if (i > start && arr[i] == arr[i - 1]) {
        continue;
      }

      // set the state
      path.emplace_back(arr[i]);

      // goto next state
      solve(arr, target - arr[i], i + 1, path);

      // reset the state
      path.pop_back();
    }

    return;
  }

  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {

    // to avoid duplicates
    sort(candidates.begin(), candidates.end());

    vector<int> path;
    solve(candidates, target, 0, path);

    return ans;
  }
};