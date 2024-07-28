class Solution {
public:
  vector<vector<int>> mat;
  int n, m;

  int xdel[4] = {0, 0, 1, -1};
  int ydel[4] = {1, -1, 0, 0};

  bool withinBounds(int x, int y) {
    return (x >= 0 && x < n && y >= 0 && y < m);
  }

  vector<pair<int, int>> solve(int x, int y, vector<vector<bool>> &vis) {
    queue<pair<int, int>> q;
    q.push({x, y});
    vis[x][y] = true;

    vector<pair<int, int>> res;
    res.push_back({0, 0});

    while (!q.empty()) {
      int i = q.front().first;
      int j = q.front().second;
      q.pop();

      for (int k = 0; k < 4; k++) {
        int r = i + xdel[k];
        int c = j + ydel[k];

        if (withinBounds(r, c) && !vis[r][c] && mat[r][c] == 1) {
          q.push({r, c});
          vis[r][c] = true;
          res.push_back({r - x, c - y});
        }
      }
    }

    return res;
  }

  int countDistinctIslands(vector<vector<int>> &grid) {
    mat = grid;
    n = mat.size();
    m = mat[0].size();

    set<vector<pair<int, int>>> res;
    vector<vector<bool>> vis(n, vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (mat[i][j] == 1 && !vis[i][j]) {
          auto nodes = solve(i, j, vis);
          res.insert(nodes);
        }
      }
    }

    return res.size();
  }
};
