class Solution {
public:
  int maxScore(vector<int> &arr, int k) {
    int n = arr.size();
    int sum = 0, minSum = 0;
    int left = 0, total = 0;

    // Need to find a subarray of lenth (n - k) with minimum sum ?

    for (int i = 0; i < n - k; ++i) {
      sum += arr[i];
      total += arr[i];
    }

    minSum = sum;

    for (int right = n - k; right < n; ++right) {

      sum += arr[right];
      sum -= arr[left];
      left++;

      minSum = min(minSum, sum);
      total += arr[right];
    }

    return total - minSum;
  }
};