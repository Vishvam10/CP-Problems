class Solution {
public:
  int missingNumber(vector<int> &arr) {
    int n = arr.size();
    int s = (n * (n + 1)) / 2;
    return s - accumulate(arr.begin(), arr.end(), 0);
  }
};