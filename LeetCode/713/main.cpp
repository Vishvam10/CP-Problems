class Solution {
public:
  int numSubarrayProductLessThanK(vector<int> &arr, int k) {

    int n = arr.size();
    int left = 0, prod = 1, ans = 0;

    for (int i = 0; i < n; i++) {
      prod *= arr[i];
      while (left <= i && prod >= k) {
        prod /= arr[left];
        left++;
      }
      ans += (i - left + 1);
    }
    return ans;
  }
};