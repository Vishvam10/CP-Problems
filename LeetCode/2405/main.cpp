class Solution {
public:
  int partitionString(string s) {

    int n = s.length();
    int ans = 0;

    unordered_map<char, bool> mp;

    for (int i = 0; i < n; i++) {
      if (mp.find(s[i]) != mp.end()) {
        ans++;
        mp.clear();
      }
      mp[s[i]] = true;
    }

    return ans + 1;
  }
};