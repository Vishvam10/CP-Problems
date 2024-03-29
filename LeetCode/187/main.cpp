class Solution {
public:
  vector<string> findRepeatedDnaSequences(string s) {
    int n = s.length();
    vector<string> ans;
    unordered_map<string, int> mp;

    for (int i = 0; i <= n; i++) {
      string temp = s.substr(i, 10);
      if (mp[temp] != -1) {
        mp[temp]++;
      }
      if (mp[temp] > 1) {
        ans.push_back(temp);
        mp[temp] = -1;
      }
    }
    return ans;
  }
};