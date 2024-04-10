class Solution {
public:
  int minSubArrayLen(int target, vector<int> &arr) {

    int n = arr.size();
    int left = 0;
    int ans = INT_MAX;
    int s = 0;

    for (int i = 0; i < n; i++) {
      if (arr[i] == target) {
        return 1;
      }
      s += arr[i];
      while (s >= target) {
        ans = min(ans, i - left + 1);
        s -= arr[left];
        left++;
      }
    }

    return (ans == INT_MAX) ? 0 : ans;
  }
};