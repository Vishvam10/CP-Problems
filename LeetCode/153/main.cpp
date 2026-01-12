class Solution {
public:
  int findMin(vector<int> &arr) {
    int n = arr.size();
    int low = 0, high = n - 1;
    int ans = INT_MAX;

    // not sorted
    if (arr[0] < arr[n - 1]) {
      return arr[0];
    }

    while (low < high) {
      int mid = low + (high - low) / 2;
      if (arr[mid] < arr[high]) {
        high = mid;
      } else {
        low = mid + 1;
      }
    }

    return arr[low];
  }
};