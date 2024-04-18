class Solution {
public:
  unordered_map<int, int> mp;
  vector<vector<int>> ans;

  void solve(vector<int> &arr, vector<int> &path) {
    if (path.size() == arr.size()) {
      ans.emplace_back(path);
      return;
    }

    for (auto it = mp.begin(); it != mp.end(); it++) {

      if (mp[it->first] > 0) {

        // set the state
        path.emplace_back(it->first);
        mp[it->first]--;

        // goto next state
        solve(arr, path);

        // reset the state
        path.pop_back();
        mp[it->first]++;
      }
    }
    return;
  }

  vector<vector<int>> permuteUnique(vector<int> &arr) {

    int n = arr.size();
    vector<int> path;

    for (int i = 0; i < n; i++) {
      mp[arr[i]]++;
    }

    solve(arr, path);

    return ans;
  }
};