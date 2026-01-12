class Solution {
public:
  int beautySum(string s) {
    int n = s.length();
    int ans = 0;

    for (int i = 0; i < n; ++i) {
      unordered_map<char, int> mp;
      for (int j = i; j < n; ++j) {
        mp[s[j]]++;
        int min_val = INT_MAX, max_val = INT_MIN;
        for (auto i : mp) {
          int val = i.second;
          if (val <= min_val) {
            min_val = val;
          }
          if (val >= max_val) {
            max_val = val;
          }
        }
        ans += (max_val - min_val);
      }
    }

    return ans;
  }
};
