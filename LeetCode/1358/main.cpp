class Solution {
public:
  int numberOfSubstrings(string s) {
    int ca = 0, cb = 0, cc = 0;
    int n = s.length(), left = 0, ans = 0;

    for (int i = 0; i < n; i++) {
      char ch = s[i];
      if (ch == 'a') {
        ca++;
      } else if (ch == 'b') {
        cb++;
      } else {
        cc++;
      }
      while (ca > 0 && cb > 0 && cc > 0) {
        ans += (n - i);
        if (s[left] == 'a') {
          ca--;
        } else if (s[left] == 'b') {
          cb--;
        } else {
          cc--;
        }
        left++;
      }
    }
    return ans;
  }
};