class Solution {
public:
  int shipWithinDays(vector<int> &arr, int days) {
    int n = arr.size();
    int low = *max_element(arr.begin(), arr.end());
    int high = accumulate(arr.begin(), arr.end(), 0);
    int ans = 0;

    auto num_days = [&](const int cap) {
      int cnt = 0, res = 0;
      for (int i = 0; i < n; ++i) {
        if (cnt < arr[i]) {
          res++;
          cnt = cap;
        }
        cnt -= arr[i];
      }
      return res;
    };

    while (low <= high) {
      // This is the capacity
      int mid = low + (high - low) / 2;
      int num_days_required = num_days(mid);

      if (num_days_required > days) {
        low = mid + 1;
      } else {
        ans = mid;
        high = mid - 1;
      }
    }

    return ans;
  }
};