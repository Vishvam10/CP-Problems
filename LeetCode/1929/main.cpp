class Solution {
public:
  vector<int> getConcatenation(vector<int> &arr) {
    int n = arr.size();
    vector<int> ans(2 * n);
    for (int i = 0; i < 2 * n; i++) {
      ans[i] = arr[i % n];
    }
    return ans;
  }
};