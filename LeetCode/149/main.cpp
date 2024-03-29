class Solution {
public:
  int maxPoints(vector<vector<int>> &arr) {

    int n = arr.size();
    int ans = 0;
    unordered_map<int, int> mp;

    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        int slope = 0;
        int x1 = arr[i][0], x2 = arr[j][0];
        int y1 = arr[i][1], y2 = arr[j][1];
        int dx = x2 - x1, dy = y2 - y1;
        if (dx == 0) {
          slope = INT_MAX;
        } else {
          slope = (dy / dx);
        }
        cout << "slope b/w" << i << " and " << j << " : " << slope << "\n";
        mp[slope]++;
      }
    }

    for (auto x : mp) {
      cout << "key : " << x.first << " value : " << x.second << "\n";
    }

    for (auto x : mp) {
      ans = max(ans, x.second);
    }

    return ans;
  }
};