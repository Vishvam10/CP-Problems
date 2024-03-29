class Solution {
public:
  int numSubarraysWithSum(vector<int> &arr, int goal) {
    int n = arr.size();
    int c = 0, left = 0, temp = 0, ans = 0;

    for (int i = 0; i < arr.size(); i++) {
      ;
      c += arr[i];

      while (c > goal) {
        c -= arr[left];
        left++;
      }

      while ((temp < i) && (temp < left || arr[temp] == 0)) {
        temp++;
      }

      if (c == goal) {
        ans += (temp - left + 1);
      }
    }

    return ans;
  }
};