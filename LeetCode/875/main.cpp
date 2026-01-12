class Solution {
public:
  int minEatingSpeed(vector<int> &arr, int h) {
    int n = arr.size();

    sort(arr.begin(), arr.end());
    int mx = arr[n - 1];

    if (h == n) {
      return mx;
    }

    // [3, 6, 7, 11] and h = 8. To find : min k
    // 0, 3, 4, 8
    //    0, 1, 5
    //       0, 2
    //          0
    // total turns = ceil(3/3) + ceil(6/3) + ceil(7/3) + ceil(11/3)
    //             = 1 + 2 + 3 + 4 = 10

    int low = 1, high = mx, ans = mx;

    while (low <= high) {
      int mid = low + (high - low) / 2;

      long long int tot = 0;
      for (int i = 0; i < n; ++i) {
        double div = ceil((double)arr[i] / mid);
        tot += div;
        if (tot > h) {
          break;
        }
      }

      if (tot <= h) {
        ans = mid;
        high = mid - 1;
      } else if (tot > h) {
        low = mid + 1;
      }
    }

    return ans;
  }
};