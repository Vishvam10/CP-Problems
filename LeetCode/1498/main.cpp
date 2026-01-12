class Solution {
public:
  const int MOD = 1e9 + 7;

  int numSubseq(vector<int> &arr, int target) {

    int n = arr.size();
    sort(arr.begin(), arr.end());

    int left = 0, right = n - 1;
    long long int ans = 0;

    vector<int> pows(n, 1);
    for (int i = 1; i < n; ++i) {
      pows[i] = pows[i - 1] * 2 % MOD;
    }

    while (left <= right) {
      if (arr[left] + arr[right] <= target) {
        ans = (ans + pows[right - left] % MOD);
        left++;
      } else {
        right--;
      }
    }

    return ans % MOD;
  }
};
