class Solution {
public:
  int hIndex(vector<int> &arr) {

    int n = arr.size();
    int ans = 0;

    sort(arr.begin(), arr.end());

    for (int i = 0; i < n; i++) {
      int key = min(arr[i], n - i);
      ans = max(ans, key);
    }

    return ans;
  }
};