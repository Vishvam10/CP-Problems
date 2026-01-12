class Solution {
public:
  bool isPal(string s, int left, int right) {
    while (left <= right) {
      if (s[left] == s[right]) {
        left++;
        right--;
      } else {
        return false;
      }
    }
    return true;
  }

  void solve(string s, int n, int left, vector<string> path,
             vector<vector<string>> &ans) {

    if (left == s.length()) {
      ans.emplace_back(path);
      return;
    }

    for (int right = left; right < n; ++right) {
      if (isPal(s, left, right)) {
        path.emplace_back(s.substr(left, right - left + 1));
        solve(s, n, right + 1, path, ans);
        path.pop_back();
      }
    }
  }

  vector<vector<string>> partition(string s) {
    int n = s.length();
    vector<vector<string>> ans;
    vector<string> path;

    // 2 actions : split at i or don't split at i ?

    // For eg.  [a], [a b a c a a b b a]
    //                      ^ (split)
    // [a], [ab], [a c a a b b a]

    solve(s, n, 0, path, ans);

    return ans;
  }
};
