bool cmp(const vector<int> &lhs, const vector<int> &rhs) {
  if (lhs[0] < rhs[0]) {
    return true;
  }
  return false;
}

class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>> &arr) {
    int n = arr.size();
    vector<vector<int>> ans;
    sort(arr.begin(), arr.end(), cmp);

    for (int i = 0; i < n; i++) {
      int s = ans.size();
      if (s == 0 || ans[s - 1][1] < arr[i][0]) {
        ans.emplace_back(arr[i]);
      } else {
        ans[s - 1][1] = max(ans[s - 1][1], arr[i][1]);
      }
    }

    return ans;
  }
};
