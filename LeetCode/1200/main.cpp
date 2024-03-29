class Solution {
public:
  vector<vector<int>> minimumAbsDifference(vector<int> &arr) {
    vector<vector<int>> ans;
    int min_diff = INT_MAX;

    sort(arr.begin(), arr.end());

    for (int i = 0; i < arr.size() - 1; i++) {
      if (abs(arr[i] - arr[i + 1]) < min_diff) {
        min_diff = abs(arr[i] - arr[i + 1]);
      }
    }

    for (int i = 0; i < arr.size() - 1; i++) {
      if (abs(arr[i] - arr[i + 1]) == min_diff) {
        ans.emplace_back(vector<int>{arr[i], arr[i + 1]});
      }
    }

    return ans;
  }
};