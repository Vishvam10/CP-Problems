class Solution {
public:
  vector<int> asteroidCollision(vector<int> &arr) {
    vector<int> ans;
    int i = 0;
    int n = arr.size();

    while (i < n) {
      if (ans.size() == 0) {
        ans.emplace_back(arr[i]);
      } else {
        int prev = ans[ans.size() - 1];
        int cur = arr[i];

        if (prev < 0 || cur > 0) {
          ans.emplace_back(cur);
        } else {
          if (prev == abs(cur)) {
            ans.pop_back();
          } else if (prev < abs(cur)) {
            ans.pop_back();
            i--;
          }
        }
      }
      i++;
    }

    return ans;
  }
};