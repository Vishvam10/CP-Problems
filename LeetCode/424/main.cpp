class Solution {
public:
  int characterReplacement(string s, int k) {
    int n = s.length();
    int left = 0, maxi = -1, ws = 0, ans = 0;
    unordered_map<char, int> mp;

    for (int i = 0; i < n; i++) {
      mp[s[i]]++;
      maxi = max(maxi, mp[s[i]]);
      ws = i - left + 1;
      if (ws - maxi <= k) {
        ans = max(ans, i - left + 1);
      } else {
        mp[s[left]]--;
        left++;
      }
    }
    return ans;
  }
};