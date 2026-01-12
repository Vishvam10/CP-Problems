class Solution {
public:
  int maxSubArray(vector<int> &arr) {
    int n = arr.size(), sum = 0, ans = INT_MIN;
    for (int i = 0; i < n; i++) {
      sum += arr[i];
      if (ans < sum) {
        ans = sum;
      }
      if (sum < 0) {
        sum = 0;
      }
    }
    return ans;
  }
};