class Solution {
public:
  int orangesRotting(vector<vector<int>> &mat) {

    int m = mat.size();
    int n = mat[0].size();

    int dr[] = {0, 0, -1, 1};
    int dc[] = {-1, 1, 0, 0};

    int steps = 0;

    vector<vector<bool>> vis(m, vector<bool>(n, false));

    queue<pair<pair<int, int>, int>> q;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (mat[i][j] == 2) {
          vis[i][j] = true;
          q.push({{i, j}, 0});
        }
      }
    }

    while (!q.empty()) {

      int x = q.front().first.first;
      int y = q.front().first.second;
      int t = q.front().second;

      steps = max(steps, t);

      q.pop();

      vector<pair<int, int>> neighbours;

      for (int i = 0; i < 4; i++) {
        int r = x + dr[i];
        int c = y + dc[i];

        if ((r >= 0 && r < m && c >= 0 && c < n) &&
            (!vis[r][c] && mat[r][c] == 1)) {
          vis[r][c] = true;
          q.push({{r, c}, t + 1});
        }
      }
    }

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (!vis[i][j] && mat[i][j] == 1) {
          return -1;
        }
      }
    }

    return steps;
  }
};