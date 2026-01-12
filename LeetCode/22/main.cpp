class Solution {
public:
  void gen(string s, int n, int open, int close, vector<string> &ans) {

    if (s.length() == 2 * n) {
      ans.emplace_back(s);
      return;
    }

    if (open < n) {
      // Add (
      gen(s + "(", n, open + 1, close, ans);
    }

    if (close < open) {
      // Add )
      gen(s + ")", n, open, close + 1, ans);
    }

    return;
  }

  vector<string> generateParenthesis(int n) {
    vector<string> ans;
    string s = "";

    gen(s, n, 0, 0, ans);

    return ans;
  }
};
