class Solution {
public:
  vector<vector<int>> ans;

  void helper(vector<int> &path, int pos, int k, int target) {
    if (k == 0) {
      if (target == 0) {
        ans.emplace_back(path);
      }
      return;
    }

    for (int i = pos; i < 10; i++) {

      // set state
      path.emplace_back(i);

      // goto next state
      helper(path, i + 1, k - 1, target - i);

      // reset state
      path.pop_back();
    }

    return;
  }

  vector<vector<int>> combinationSum3(int k, int n) {
    vector<int> path;

    helper(path, 1, k, n);

    return ans;
  }
};