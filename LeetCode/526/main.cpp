class Solution {
public:
  int ans = 0;

  void solve(vector<int> &arr, int n, int num) {
    if (num == n + 1) {
      ans++;
      return;
    }

    for (int i = 1; i <= n; i++) {
      if (arr[i] == 0 && (num % i == 0 || i % num == 0)) {

        // set the state
        arr[i] = num;

        // goto next state
        solve(arr, n, num + 1);

        // reset the state
        arr[i] = 0;
      }
    }
  }

  int countArrangement(int n) {
    vector<int> arr(n + 1, 0);
    solve(arr, n, 1);

    return ans;
  }
};