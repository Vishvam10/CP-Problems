class Solution {
public:
  int s;
  int k;
  int ans = INT_MAX;

  void solve(vector<int> &arr, vector<int> &count, int start) {

    if (accumulate(count.begin(), count.end(), 0) == s) {
      ans = min(ans, *max_element(count.begin(), count.end()));
      return;
    }

    for (int i = start; i < arr.size(); i++) {

      // k choices
      for (int child = 0; child < k; child++) {

        // set the state (assign to kth child)
        count[child] += arr[i];

        // goto next state
        solve(arr, count, i + 1);

        // reset the state (don't assign to the kth child)
        count[child] -= arr[i];
      }
    }
    return;
  }

  int distributeCookies(vector<int> &arr, int _k) {

    s = accumulate(arr.begin(), arr.end(), 0);
    k = _k;

    vector<int> count(k, 0);

    solve(arr, count, 0);

    return ans;
  }
};