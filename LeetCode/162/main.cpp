class Solution {
public:
  int findPeakElement(vector<int> &arr) {
    int n = arr.size();
    if (n == 1) {
      return 0;
    }
    if (arr[0] > arr[1]) {
      return 0;
    }
    if (arr[n - 1] > arr[n - 2]) {
      return n - 1;
    }

    int low = 1, high = n - 2;

    while (low <= high) {
      int mid = low + (high - low) / 2;

      // mid is peak
      if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]) {
        return mid;
      }
      // mid is left of peak => go right
      else if (arr[mid] < arr[mid + 1]) {
        low = mid + 1;
      }
      // mid is right of peak => go left
      else if (arr[mid] < arr[mid - 1]) {
        high = mid - 1;
      }
    }
    return -1;
  }
};