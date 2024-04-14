class Solution {
public:
  int largestSumAfterKNegations(vector<int> &arr, int k) {

    int n = arr.size();

    sort(arr.begin(), arr.end());

    for (int i = 0; i < n; i++) {
      if (arr[i] < 0 && k > 0) {
        arr[i] = -arr[i];
        k--;
      }
    }

    sort(arr.begin(), arr.end());

    if (k % 2 == 1) {
      arr[0] = -arr[0];
    }

    return accumulate(arr.begin(), arr.end(), 0);
  }
};