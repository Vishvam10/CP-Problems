class Solution {
public:
  double findMaxAverage(vector<int> &arr, int k) {
    int n = arr.size(), left = 0;
    double s = 0, ans = 0;

    for (int i = 0; i < k; i++) {
      s += arr[i];
    }

    ans = s / k;

    for (int i = k; i < n; i++) {
      s -= arr[left];
      s += arr[i];
      left++;
      ans = max(ans, s / k);
    }

    return ans;
  }
};