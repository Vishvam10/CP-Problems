class Solution {
public:
  int helper(vector<int> &arr, int target, bool first) {

    int low = 0, high = arr.size() - 1;
    int ans = -1;

    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (arr[mid] == target) {
        ans = mid;
        if (flag) {
          high = mid - 1;
        } else {
          low = mid + 1;
        }
      } else if (arr[mid] > target) {
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return ans;
  }

  vector<int> searchRange(vector<int> &arr, int target) {
    return {helper(arr, target, true), helper(arr, target, false)};
  }
};