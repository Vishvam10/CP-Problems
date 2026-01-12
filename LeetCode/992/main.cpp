class Solution {
public:
  int atMost(vector<int> &arr, int k) {
    int n = arr.size();
    int left = 0, right = 0, cnt = 0, ans = INT_MIN;
    unordered_map<int, int> mp;

    while (right < n) {

      if (mp[arr[right]] == 0)
        cnt++;
      mp[arr[right]]++;

      while (cnt > k) {
        mp[arr[left]]--;
        if (mp[arr[left]] == 0)
          cnt--;
        left++;
      }

      ans += right - left + 1;
      right++;
    }

    return ans;
  }

  int subarraysWithKDistinct(vector<int> &arr, int k) {
    return atMost(arr, k) - atMost(arr, k - 1);
  }
};