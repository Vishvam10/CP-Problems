class Solution {
public:
  int subsetXORSum(vector<int> &arr) {
    int n = arr.size();
    int ans = 0;

    for (int i = 0; i < (1 << n); i++) {
      int s = 0;
      for (int j = 0; j < n; j++) {
        if (i & (1 << j)) {
          s ^= arr[j];
        }
      }
      ans += s;
    }
    return ans;
  }
};