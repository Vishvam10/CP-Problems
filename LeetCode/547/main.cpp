class Solution {
public:
  void dfs(int node, vector<vector<int>> &adj, vector<bool> &vis) {
    for (int i = 0; i < adj.size(); i++) {
      if (adj[node][i] != 0 && !vis[i]) {
        vis[i] = true;
        dfs(i, adj, vis);
      }
    }
  }

  void bfs(int start, vector<vector<int>> &adj, vector<bool> &vis) {

    queue<int> q;
    q.push(start);

    while (!q.empty()) {
      int node = q.front();
      q.pop();

      for (int i = 0; i < adj.size(); i++) {
        if (adj[node][i] != 0 && !vis[i]) {
          vis[i] = true;
          q.push(i);
        }
      }
    }
  }

  int findCircleNum(vector<vector<int>> &adj) {

    int n = adj.size();
    int ans = 0;

    vector<bool> vis(n + 1, false);

    for (int i = 0; i < n; i++) {
      if (!vis[i]) {
        ans++;
        bfs(i, adj, vis);
      }
    }

    return ans;
  }
};