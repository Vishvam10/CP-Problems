class Solution {
public:
  int findKthPositive(vector<int> &arr, int k) {
    int n = arr.size();

    if (k < arr[0]) {
      return k;
    }

    // 0 1 2 3 4
    // 2 3 4 7 11
    // 1 2 3 4 5
    // 1 1 1 3 6 := 5
    //       h l
    //         m

    // 0 1
    // 1 2
    // 1 2
    // 0 0
    //   h
    //   l
    //   m

    int low = 0, high = n - 1;

    while (low <= high) {
      int mid = low + (high - low) / 2;
      int res = arr[mid] - (mid + 1);
      if (res >= k) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    // int offset = k - (arr[high] - (high + 1))
    // int ans = arr[high] + offset = k + high + 1

    return k + high + 1;
  }
};